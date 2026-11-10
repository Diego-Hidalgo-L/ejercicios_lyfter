from ioc_container import ioc
from db import User, BillingAddress, PaymentMethod, UserPaymentMethod, Product, Cart, CartProduct, Invoice, InvoiceProduct
from validations import validate_user, validate_owner, validate_admin, validate_owner_or_admin
from services import Transaction
from cache_functions import check_if_cache, invalidate_cache

from flask import Flask, request, jsonify
from argon2.exceptions import VerifyMismatchError
import json


app = Flask("e-commerce")


# ------------------- ADMIN start -------------------
@app.route("/refresh-token", methods=["POST"])
def refresh_token():
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_user(token)

        if validation is not True:
            return validation, decoded

        if token is None:
            return jsonify(error_message="Invalid token"), 401

        decoded = ioc.jwt_manager.decode(token)

        if decoded is None:
            return jsonify(error_message="Error decoding token"), 401

        if decoded['token_type'] != "refresh":
            return jsonify(error_message="Invalid token type provided"), 400

        user_id = decoded['id']
        access_token = ioc.jwt_manager.encode(user_id, "access")

        if access_token is None:
            return jsonify(error_message="Error encoding access token"), 401

        return jsonify(access_token=access_token), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error creating access token: {error}"), 500

# ------------------- ADMIN end -------------------


# ------------------- USERS start -------------------
@app.route("/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        full_name = data.get('full_name')

        if username is None or password is None:
            return jsonify(error_message="Invalid credentials"), 400
        
        hashed_password = ioc.ph.hash(password)
        new_user = User(username=username, password=hashed_password, email=email, full_name=full_name, role='User')
        result = new_user.add()

        if result is False:
            return jsonify(error_message="Error inserting user into the database"), 500

        user_id = result.id
        access_token = ioc.jwt_manager.encode(user_id, "access")
        refresh_token = ioc.jwt_manager.encode(user_id, "refresh")

        if access_token is None:
            return jsonify(error_message="Error encoding token"), 401

        elif refresh_token is None:
            return jsonify(error_message="Error encoding refresh token"), 401

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("users", "all")
        
        return jsonify(access_token=access_token, refresh_token=refresh_token), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error registering user: {error}"), 500


@app.route("/login", methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return jsonify(error_message="Invalid credentials"), 400
        
        user = User.get_by_username(username)

        if user is None:
            return jsonify(error_message="User not found"), 404
        elif user is False:
            raise Exception

        user_id = user.id
        stored_hash = user.password

        try:
            ioc.ph.verify(stored_hash, password)
        except VerifyMismatchError:
            return jsonify(error_message="Invalid credentials"), 400

        access_token = ioc.jwt_manager.encode(user_id, "access")
        refresh_token = ioc.jwt_manager.encode(user_id, "refresh")

        if access_token is None:
            return jsonify(error_message="Error encoding access token"), 401
        
        elif refresh_token is None:
            return jsonify(error_message="Error encoding refresh token"), 401

        return jsonify(access_token=access_token, refresh_token=refresh_token), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error logging in: {error}"), 500


@app.route("/users", methods=["GET"])         # Después implementar filters
def get_all_users():
    try:
        token = request.headers.get("Authorization")
        validation = validate_admin(token)

        if validation is not True:
            return validation

        # IF CACHE:
        users_key = ioc.cache_manager.generate_key("users", "all")
        cache_result = check_if_cache(users_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            users = User.get_all()

            if users is None:
                return jsonify(error_message=f"No users found"), 404
            elif users is False:
                raise Exception

            # STORE CACHE:
            ioc.cache_manager.store_data(users_key, json.dumps(users, default=str), 300)

            return jsonify(users), 200
        
    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting all users: {error}"), 500


@app.route("/me/<identifier>", methods=["GET"])
def me(identifier):
    try:
        token = request.headers.get('Authorization')
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        me_key = ioc.cache_manager.generate_users_key(identifier, "me", identifier)
        cache_result = check_if_cache(me_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            user_id = decoded['id']
            user = User.get_by_id(identifier)

            if user is None:
                return jsonify(error_message=f"User ID {identifier} not found"), 404
            elif user is False:
                raise Exception

            username = user.username
            role = user.role

            # STORE CACHE:
            ioc.cache_manager.store_data(me_key, json.dumps({"id":user_id, "username":username, "role":role}), ttl=300)

            return jsonify(id=user_id, username=username, role=role), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error accessing user profile: {error}"), 500


@app.route("/users/<identifier>", methods=["PATCH"])
def update_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        user = User.get_by_id(identifier)

        if not user:
            return jsonify(error_message=f"User ID {identifier} not found"), 404

        user_id = decoded['id']
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        update_result = user.update(username=username, password=password)

        if update_result is not True:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("me", item_id=identifier, identifier=identifier)
        invalidate_cache("users", "all")
        
        return jsonify(message=f"User ID {user_id} updated successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user ID {identifier}: {error}"), 500


@app.route("/users/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner_or_admin(token, identifier)

        if validation is not True:
            return validation, decoded

        user = User.get_by_id(identifier)

        if not user:
            return jsonify(error_message=f"User ID {identifier} not found"), 404

        user_id = decoded['id']
        delete_result = user.delete()

        if delete_result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("me", item_id=identifier, identifier=identifier)
        invalidate_cache("users", "all")

        return jsonify(message=f"User ID {user_id} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user ID {identifier}: {error}"), 500

# ------------------- USERS end -------------------


# ------------------- BILLING ADDRESS start -------------------
@app.route("/me/<identifier>/billing", methods=["POST"])
def add_billing_address(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        data = request.get_json()
        user_id = decoded['id']
        address = data.get("address")

        billing_address = BillingAddress(user_id=user_id, address=address)
        new_billing_address = billing_address.add()

        if new_billing_address is False:
            return jsonify(error_message=f"Error adding billing address to the database"), 500

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("billing_addresses", identifier=identifier)

        return jsonify(id=new_billing_address.id, user_id=new_billing_address.user_id, address=new_billing_address.address), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error registering billing address for user ID {identifier}: {error}"), 500


@app.route("/me/<identifier>/billing/<billing_id>", methods=["GET"])
def get_one_billing_address(identifier, billing_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner_or_admin(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        billing_key = ioc.cache_manager.generate_users_key(identifier, "billing_addresses", billing_id)
        cache_result = check_if_cache(billing_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            billing_address = BillingAddress.get_by_id(billing_id)

            if billing_address.user_id != decoded['id']:
                return jsonify(error_message="Cannot access page"), 403

            if billing_address is None:
                return jsonify(error_message="No billing addresses found"), 404
            elif billing_address is False:
                raise Exception

            # STORE CACHE:
            ioc.cache_manager.store_data(billing_key, json.dumps(billing_address, default=str), 300)

            return billing_address.format_dict(), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's billing addresses (user ID: {identifier}): {error}"), 500


@app.route("/me/<identifier>/billing", methods=["GET"])
def get_my_billing_addresses(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner_or_admin(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        billing_key = ioc.cache_manager.generate_users_key(identifier, "billing_addresses")
        cache_result = check_if_cache(billing_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            billing_addresses = BillingAddress.get_all_by_user_id(decoded['id'])

            if billing_addresses is None:
                return jsonify(error_message="No billing addresses found"), 404
            elif billing_addresses is False:
                raise Exception

            # STORE CACHE:
            ioc.cache_manager.store_data(billing_key, json.dumps(billing_addresses, default=str), 300)

            return billing_addresses, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's billing addresses (user ID: {identifier}): {error}"), 500


@app.route("/me/<identifier>/billing/<billing_id>", methods=["PATCH"])
def update_billing_address(identifier, billing_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        billing_address = BillingAddress.get_by_id(billing_id)

        if billing_address is None:
            return jsonify(error_message="No billing addresses found"), 404
        elif billing_address is False:
            raise Exception

        data = request.get_json()
        new_address = data.get('address')

        update_result = billing_address.update(new_address)

        if update_result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("billing_addresses", item_id=billing_id, identifier=identifier)

        return jsonify(message=f"Billing address for user ID {identifier} updated successfully"), 200
        
    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user's (ID: {identifier}) billing address: {error}"), 500


@app.route("/me/<identifier>/billing/<billing_id>", methods=["DELETE"])
def delete_billing_address(identifier, billing_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        billing_address = BillingAddress.get_by_id(billing_id)

        if billing_address is None:
            return jsonify(error_message=f"Billing address ID {identifier} not found"), 404
        elif billing_address is False:
            raise Exception

        delete_result = billing_address.delete()

        if delete_result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("billing_addresses", item_id=billing_id, identifier=identifier)

        return jsonify(message=f"Billing address for user ID {identifier} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user's (ID: {identifier}) billing address: {error}"), 500


# ------------------- BILLING ADDRESS end -------------------


# ------------------- PAYMENT METHODS start -------------------
@app.route("/payment_methods", methods=["POST"])
def add_payment_method():
    try:
        token = request.headers.get("Authorization")
        validation = validate_admin(token)

        if validation is not True:
            return validation

        data = request.get_json()
        method_name = data.get('method_name')

        payment_method = PaymentMethod(method_name=method_name)
        result = payment_method.add()

        if result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("payment_methods", "all")

        return jsonify(message="Payment method added successfully"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error adding payment method: {error}"), 500


@app.route("/payment_methods", methods=["GET"])
def get_all_payment_methods():
    token = request.headers.get("Authorization")
    validation, decoded = validate_user(token)

    if validation is not True:
        return validation, decoded

    # IF CACHE:
    all_methods_key = ioc.cache_manager.generate_key("payment_methods", "all")
    cache_result = check_if_cache(all_methods_key)

    if cache_result is not None:
        return cache_result

    # ELIF NO CACHE:
    else:
        payment_methods = PaymentMethod.get_all()

        if payment_methods is None:
            return jsonify(error_message=f"No products found"), 404
        elif payment_methods is False:
            raise Exception

        # STORE CACHE:
        ioc.cache_manager.store_data(all_methods_key, json.dumps(payment_methods, default=str), 3600)

        return jsonify(payment_methods), 200


@app.route("/me/<identifier>/payment_methods", methods=["POST"])
def add_my_payment_method(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        data = request.get_json()
        user_id = decoded['id']
        payment_method_id = data.get('payment_method_id')
        alias = data.get('alias')
        is_default = data.get('is_default')

        my_payment_method = UserPaymentMethod(user_id=user_id, payment_method_id=payment_method_id, alias=alias, is_default=is_default)
        result = my_payment_method.add()

        if result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("payment_methods", identifier=identifier)

        return jsonify(message=f"Payment method added successfully for user ID {user_id}"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error adding payment method for user ID {identifier}: {error}"), 500


@app.route("/me/<identifier>/payment_methods", methods=["GET"])
def get_my_payment_methods(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        my_methods_key = ioc.cache_manager.generate_users_key(identifier, "payment_methods")
        cache_result = check_if_cache(my_methods_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            user_payment_methods = UserPaymentMethod.get_all_by_user_id(decoded['id'])

            if user_payment_methods is None:
                return jsonify("No payment methods found"), 404
            elif user_payment_methods is False:
                raise Exception

            # STORE CACHE:
            ioc.cache_manager.store_data(my_methods_key, json.dumps(user_payment_methods, default=str), 300)

            return user_payment_methods, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's payment methods (user ID: {identifier}): {error}"), 500


@app.route("/me/<identifier>/payment_methods/<payment_method_id>", methods=["PATCH"])
def update_user_payment_method(identifier, payment_method_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        user_id = decoded['id']
        payment_method = UserPaymentMethod.get_by_id(payment_method_id)

        if payment_method is None:
            return jsonify(error_message="No payment methods found"), 404
        elif payment_method is False:
            raise Exception
        elif payment_method.user_id != user_id:
            return jsonify(error_message=f"Cannot access page"), 401

        data = request.get_json()
        new_alias = data.get('alias')
        is_default = data.get('is_default')

        result = payment_method.update(new_alias, is_default)

        if result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("payment_methods", item_id=payment_method_id, identifier=identifier)

        return jsonify(message=f"Payment method for user ID {identifier} updated successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user's (ID: {identifier}) payment method: {error}"), 500


@app.route("/me/<identifier>/payment-methods/<payment_method_id>", methods=["DELETE"])
def delete_user_payment_method(identifier, payment_method_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        user_id = decoded['id']
        payment_method = UserPaymentMethod.get_by_id(payment_method_id)

        if payment_method is None:
            return jsonify(error_message=f"Payment method ID {payment_method_id} not found"), 404
        elif payment_method is False:
            raise Exception
        elif payment_method.user_id != user_id:
            return jsonify(error_message="Cannot access page"), 401

        delete_result = payment_method.delete()

        if delete_result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("payment_methods", item_id=payment_method_id, identifier=identifier)

        return jsonify(message=f"Payment method for user ID {identifier} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user's (ID: {identifier}) payment method: {error}"), 500


# ------------------- PAYMENT METHODS end -------------------


# ------------------- PRODUCTS start -------------------
@app.route("/products", methods=['POST'])
def add_product():
    try:
        token = request.headers.get("Authorization")
        validation = validate_admin(token)

        if validation is not True:
            return validation

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        new_product = Product(name=name, price=price, entry_date=entry_date, stock=stock)
        result = new_product.add()

        if result is False:
            return jsonify(error_message=f"Error inserting product into the database"), 500

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("products", "all")

        return jsonify(message=f"Product '{new_product.name}' added successfully"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error inserting product: {error}"), 500


@app.route("/products", methods=["GET"])
def get_all_products():
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_user(token)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        products_key = ioc.cache_manager.generate_key("products", "all")
        cache_result = check_if_cache(products_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            products = Product.get_all()

            if products is None:
                return jsonify(error_message=f"No products found"), 404
            elif products is False:
                raise Exception

            # STORE CACHE:
            ioc.cache_manager.store_data(products_key, json.dumps(products, default=str), 900)

            return jsonify(products), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting all products: {error}"), 500


@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_user(token)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        product_key = ioc.cache_manager.generate_key("products", product_id)
        cache_result = check_if_cache(product_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            product = Product.get_by_id(product_id)

            if product is None:
                return jsonify(error_message=f"Product ID {product_id} not found"), 404
            elif product is False:
                raise Exception

            # STORE CACHE:
            formatted_product = product.format_dict()
            ioc.cache_manager.store_data(product_key, json.dumps(formatted_product), 600)

            return product.format_dict(), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting product ID {product_id}: {error}"), 500


@app.route("/products/<product_id>", methods=["PATCH"])
def update_product(product_id):
    try:
        token = request.headers.get("Authorization")
        validation = validate_admin(token)

        if validation is not True:
            return validation

        product = Product.get_by_id(product_id)

        if product is None:
            return jsonify(error_message=f"Product ID {product_id} not found"), 404
        elif product is False:
            raise Exception

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        result = product.update(name=name, price=price, entry_date=entry_date, stock=stock)

        if result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("products", item_id=product_id)

        return jsonify(message=f"Product ID {product_id} updated successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating product ID {product_id}: {error}"), 500


@app.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        token = request.headers.get("Authorization")
        validation = validate_admin(token)

        if validation is not True:
            return validation

        product = Product.get_by_id(product_id)

        if product is None:
            return jsonify(error_message=f"Product ID {product_id} not found"), 404
        elif product is False:
            raise Exception

        result = product.delete()

        if result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("products", item_id=product_id)

        return jsonify(message=f"Product ID {product_id} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting product ID {product_id}: {error}"), 500

# ------------------- PRODUCTS end -------------------


# ------------------- INVOICES start -------------------
@app.route("/me/<identifier>/invoices", methods=["GET"])
def get_my_invoices(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner_or_admin(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        invoices_key = ioc.cache_manager.generate_users_key(identifier, "invoices")
        cache_result = check_if_cache(invoices_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            invoices = Invoice.get_all_by_user_id(decoded['id'])

            if invoices is None:
                return jsonify(error_message="No invoices found"), 404
            elif invoices is False:
                raise Exception

            # STORE CACHE:
            ioc.cache_manager.store_data(invoices_key, json.dumps(invoices, default=str), 1200)

            return invoices, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's invoices (user ID: {identifier}): {error}"), 500


@app.route("/me/<identifier>/invoices/<invoice_id>", methods=["GET"])
def get_invoice_by_id(identifier, invoice_id):
    try:
        token = request.headers.get("Authorization")

        # IF CACHE:
        invoice_key = ioc.cache_manager.generate_users_key(identifier, "invoices", item_id=invoice_id)
        cache_result = check_if_cache(invoice_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            invoice = Invoice.get_by_id(invoice_id)

            if invoice is None:
                return jsonify(error_message=f"Invoice ID {identifier} not found"), 404
            if invoice is False:
                raise Exception

            validation, decoded = validate_owner_or_admin(token, invoice.user_id)

            if validation is not True:
                return validation, decoded

            products = InvoiceProduct.get_by_invoice_id(invoice.id)
            billing_address = BillingAddress.get_by_id(invoice.billing_address_id).address      # falta poder extraer un billing_id con el invoice --> guardar en nueva tabla 'purchase'
            user_payment_method = UserPaymentMethod.get_by_id(invoice.user_payment_method_id).alias    #falta poder extraer un user_payment_method con el invoice --> guardar en nueva tabla 'purchase'

            # STORE CACHE:
            ioc.cache_manager.store_data(invoice_key, json.dumps({"id":invoice.id, "user_id":invoice.user_id, "products":products, "purchase_date":invoice.purchase_date, "billing_address":billing_address, "user_payment_method":user_payment_method, "status":invoice.status}, default=str), 1200)

            return jsonify(id=invoice.id, user_id=invoice.user_id, products=products, purchase_date=invoice.purchase_date, billing_address=billing_address, user_payment_method=user_payment_method, status=invoice.status), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting invoice ID {identifier}: {error}"), 500

# ------------------- INVOICES end -------------------


# ------------------- CARTS start -------------------
@app.route("/me/<identifier>/carts", methods=["POST"])
def add_active_cart(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        user_id = decoded['id']
        my_cart = Cart.get_or_create_active_cart(user_id)

        if my_cart is False:
            raise Exception("Error creating active cart")

        cart_products = CartProduct.get_by_cart_id(my_cart.id)

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("carts", identifier=identifier)

        return jsonify(my_cart.format_dict(cart_products)), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error adding cart: {error}"), 500


@app.route("/me/<identifier>/carts", methods=["GET"])
def get_all_my_carts(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        carts_key = ioc.cache_manager.generate_users_key(identifier, "carts")
        cache_result = check_if_cache(carts_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        else:
            user_id = decoded['id']
            my_carts = Cart.get_all_by_user_id(user_id)

            if my_carts is None:
                return jsonify(error_message="No carts found"), 404
            elif my_carts is False:
                raise Exception("Error getting carts from the database")

            # STORE CACHE:
            ioc.cache_manager.store_data(carts_key, json.dumps(my_carts, default=str), 180)

            return my_carts, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting all carts: {error}"), 500


@app.route("/me/<identifier>/carts/<cart_id>", methods=["GET"])
def get_my_cart(identifier, cart_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        # IF CACHE:
        cart_key = ioc.cache_manager.generate_users_key(identifier, "carts", cart_id)
        cache_result = check_if_cache(cart_key)

        if cache_result is not None:
            return cache_result

        # ELIF NO CACHE:
        user_id = decoded['id']
        my_cart = Cart.get_by_id_dict(cart_id)

        if my_cart is None:
            return jsonify(error_message=f"Cart ID {cart_id} not found"), 404
        elif my_cart is False:
            raise Exception(f"Error getting cart ID {cart_id} from the database")
        elif my_cart.get('user_id') != user_id:
            return jsonify(error_message=f"Cannot access page"), 403

        # STORE CACHE:
        ioc.cache_manager.store_data(cart_key, json.dumps(my_cart, default=str), 180)

        return jsonify(my_cart), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting cart ID {cart_id}: {error}"), 500


@app.route("/me/<identifier>/carts/<cart_id>", methods=["PUT"]) # ATENCIÓN: Al no estar atado a un session, se pueden generar cambios desligados entre tablas.
def update_my_cart(identifier, cart_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        user_id = decoded['id']
        my_cart = Cart.get_by_id_obj(cart_id)
        print(user_id)
        print(cart_id)

        if my_cart is None:
            return jsonify(error_message=f"Cart ID {cart_id} not found"), 404
        elif my_cart is False:
            raise Exception(f"Error getting cart ID {cart_id}")
        elif my_cart.user_id != user_id:
            return jsonify(error_message="Invalid cart"), 401
        elif my_cart.status == 'Completed':
            return jsonify(error_message="Cart already completed"), 400

        data = request.get_json()
        cart_products = data.get('cart_products')
        status = data.get('status')

        result = my_cart.update(cart_products=cart_products, status=status)

        if result is False:
            raise Exception

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("carts", item_id=cart_id, identifier=identifier)

        return jsonify(message=f"Cart ID {cart_id} updated successfully")

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating cart ID {cart_id}: {error}"), 500


@app.route("/me/<identifier>/carts/<cart_id>", methods=["DELETE"])
def delete_my_cart(identifier, cart_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_owner(token, identifier)

        if validation is not True:
            return validation, decoded

        user_id = decoded['id']
        my_cart = Cart.get_by_id_obj(cart_id)

        if my_cart is None:
            return jsonify(error_message=f"Cart ID {cart_id} not found"), 404
        elif my_cart is False:
            raise Exception(f"Error getting cart ID {cart_id}")
        elif my_cart.user_id != user_id:
            return jsonify(error_message=f"Invalid cart"), 401
        elif my_cart.status != 'Active':
            return jsonify(error_message="Inactive cart"), 400

        products_delete = CartProduct.delete(cart_id)
        if products_delete is False:
            raise Exception("Error deleting cart products from the database")

        cart_delete = my_cart.delete()
        if cart_delete is False:
            raise Exception("Error deleting cart from the database")

        # CHECK AND INVALIDATE CACHE:
        invalidate_cache("carts", item_id=cart_id, identifier=identifier)

        return jsonify(message=f"Cart ID {cart_id} deleted successfully")

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting cart ID {cart_id}: {error}"), 500

# ------------------- CARTS end -------------------


# ------------------- TRANSACTIONS start -------------------
@app.route("/checkout/<cart_id>", methods=["POST"])
def make_purchase(cart_id):
    try:
        token = request.headers.get("Authorization")
        validation, decoded = validate_user(token)

        if validation is not True:
            return validation, decoded

        # Data retrieval:
        user_id = decoded['id']
        data = request.get_json()
        billing_address_id = data.get('billing_address_id')
        user_payment_method_id = data.get('user_payment_method_id')

        # Execute purchase:
        result, status = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        if result is not True:
            return jsonify(error_message=result), status

        return jsonify(message="Purchase successful"), status

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error making purchase: {error}"), 500


@app.route("/return/<invoice_id>", methods=["POST"])
def return_purchase(invoice_id):
    try:
        token = request.headers.get("Authorization")
        invoice = Invoice.get_by_id(invoice_id)

        validation, decoded = validate_owner_or_admin(token, invoice.user_id)

        if validation is not True:
            return validation, decoded

        result, status = Transaction().return_purchase(invoice_id, decoded['id'])

        if result is not True:
            return jsonify(error_message=result), status

        return jsonify(message="Purchase returned successfully"), status

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error making purchase: {error}"), 500


# ------------------- TRANSACTIONS end -------------------


if __name__ == "__main__":
    app.run(host='localhost', port=7000, debug=True)