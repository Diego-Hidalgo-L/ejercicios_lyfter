from ioc_container import ioc
from db import User, Product, Invoice, BillingAddress, PaymentMethod, UserPaymentMethod
from validations import validate_admin, validate_same_user_or_admin, validate_user
from services import Transaction
from functions import generate_fake_ip

from flask import Flask, request, jsonify
from argon2.exceptions import VerifyMismatchError
from datetime import date, datetime, timezone
import json


app = Flask("e-commerce")


# ------------------- ADMIN start -------------------
@app.route("/refresh-token", methods=["POST"])
def refresh_token():
    try:
        token = request.headers.get("Authorization")

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
        # fake_ip = generate_fake_ip()        # if Login History
        # now = datetime.now(tz=timezone.utc)        # if Login History

        try:
            ioc.ph.verify(stored_hash, password)
        except VerifyMismatchError:
            # ioc.login_repo.register_login(user_id, now, fake_ip, "failed")        # if Login History
            return jsonify(error_message="Invalid credentials"), 400

        access_token = ioc.jwt_manager.encode(user_id, "access")
        refresh_token = ioc.jwt_manager.encode(user_id, "refresh")

        if access_token is None:
            # ioc.login_repo.register_login(user_id, now, fake_ip, "failed")        # if Login History
            return jsonify(error_message="Error encoding access token"), 401
        
        elif refresh_token is None:
            # ioc.login_repo.register_login(user_id, now, fake_ip, "failed")        # if Login History
            return jsonify(error_message="Error encoding refresh token"), 401

        # ioc.login_repo.register_login(user_id, now, fake_ip, "successful")        # if Login History

        return jsonify(access_token=access_token, refresh_token=refresh_token), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error logging in: {error}"), 500


@app.route("/users/all", methods=["GET"])
def get_all_users():         # Después implementar filters
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_admin(token)

        if validation_result is not True:
            return validation_result

        users = User.get_all()

        if users is None:
            return jsonify(error_message=f"No users found"), 404
        elif users is False:
            raise Exception

        return jsonify(users), 200
        
    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting all users: {error}"), 500


@app.route("/me/<identifier>", methods=["GET"])
def me(identifier):
    try:
        token = request.headers.get('Authorization')
        validation, result = validate_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        user = User.get_by_id(identifier)

        if user is None:
            return jsonify(error_message=f"User ID {identifier} not found"), 404
        elif user is False:
            raise Exception

        username = user.username
        role = user.role

        return jsonify(id=user_id, username=username, role=role), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error accessing user profile: {error}"), 500


@app.route("/users/<identifier>", methods=["PATCH"])
def update_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user = User.get_by_id(identifier)

        if not user:
            return jsonify(error_message=f"User ID {identifier} not found"), 404

        user_id = result
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        result = user.update(username=username, password=password)

        if result is False:
            return jsonify(error_message=f"Error updating user ID {user_id}"), 403
        
        return jsonify(message=f"User ID {user_id} updated successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user ID {identifier}: {error}"), 500


@app.route("/users/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user = User.get_by_id(identifier)

        if not user:
            return jsonify(error_message=f"User ID {identifier} not found"), 404

        user_id = result
        delete_result = user.delete()

        if delete_result is False:
            return jsonify(error_message=f"Error deleting user ID {user_id} from the database"), 500

        return jsonify(message=f"User ID {user_id} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user ID {identifier}: {error}"), 500

# ------------------- USERS end -------------------


# ------------------- BILLING ADDRESS start -------------------
@app.route("/me/<identifier>/billing", methods=["POST"])
def register_billing_address(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_same_user_or_admin(token, identifier)[0]

        if validation_result is not True:
            return validation_result

        data = request.get_json()
        user_id = data.get("user_id")
        address = data.get("address")

        billing_address = BillingAddress(user_id=user_id, address=address)
        new_billing_address = billing_address.add()

        if new_billing_address is False:
            return jsonify(error_message=f"Error adding billing address to the database"), 500

        return jsonify(id=new_billing_address.id, user_id=new_billing_address.user_id, address=new_billing_address.address), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error registering billing address for user ID {identifier}: {error}"), 500


@app.route("/me/<identifier>/billing", methods=["GET"])
def get_my_billing_addresses(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result, result = validate_same_user_or_admin(token, identifier)

        if validation_result is not True:
            return validation_result

        billing_addresses = BillingAddress.get_all_by_user_id(result)

        if billing_addresses is None:
            return jsonify(error_message="No billing addresses found"), 404
        elif billing_addresses is False:
            raise Exception

        return billing_addresses, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's billing addresses (user ID: {identifier}): {error}"), 500

# ------------------- BILLING ADDRESS end -------------------


# ------------------- PAYMENT METHODS start -------------------
@app.route("/payment_methods", methods=["POST"])
def add_payment_method():
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_admin(token)

        if validation_result is not True:
            return validation_result

        data = request.get_json()
        user_id = data.get('user_id')
        method = data.get('method')

        payment_method = PaymentMethod(user_id=user_id, method=method)
        result = payment_method.add()

        if result is False:
            raise Exception

        return jsonify(message="Payment method added successfully"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error adding payment method: {error}"), 500


@app.route("/me/<identifier>/payment_methods", methods=["POST"])
def add_my_payment_method(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result, result = validate_same_user_or_admin(token, identifier)

        if validation_result is not True:
            return validation_result

        data = request.get_json()
        user_id = result
        payment_method_id = data.get('payment_method_id')
        alias = data.get('alias')
        is_default = data.get('is_default')

        my_payment_method = UserPaymentMethod(user_id=user_id, payment_method_id=payment_method_id, alias=alias, is_default=is_default)
        result = my_payment_method.add()

        if result is False:
            raise Exception

        return jsonify(f"Payment method added successfully for user ID {user_id}"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error adding payment method for user ID {identifier}: {error}")


@app.route("/me/<identifier>/payment_methods")
def get_my_payment_methods(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result, result = validate_same_user_or_admin(token, identifier)

        if validation_result is not True:
            return validation_result

        payment_methods = PaymentMethod.get_all_by_user_id(result)

        if payment_methods is None:
            return jsonify("No payment methods found"), 404
        elif payment_methods is False:
            raise Exception

        return payment_methods, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's payment methods (user ID: {identifier}): {error}"), 500

# ------------------- PAYMENT METHODS end -------------------


# ------------------- PRODUCTS start -------------------
@app.route("/products/all", methods=["GET"])
def get_all_products():
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_user(token)[0]

        if validation_result is not True:
            return validation_result

        # CACHE:
        # all_key = ioc.cache_manager.generate_key("product","all")
        
        # if ioc.cache_manager.check_key(all_key)[0]:
        #     cached_data = json.loads(ioc.cache_manager.get_data(all_key))

        #     return jsonify(cached_data), 200

        # NO CACHE:
        else:
            products = Product.get_all()

            if products is None:
                return jsonify(error_message=f"No products found"), 404
            elif products is False:
                raise Exception

            # ioc.cache_manager.store_data(all_key, json.dumps(all_products, default=str))

            return jsonify(products), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting all products: {error}")


@app.route("/products/<identifier>", methods=["GET"])
def get_product(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_user(token)[0]

        if validation_result is not True:
            return validation_result

        # SINGLE PRODUCT CACHE:
        # product_key = ioc.cache_manager.generate_key("product", identifier)

        # if ioc.cache_manager.check_key(product_key)[0]:
        #     cached_data = json.loads(ioc.cache_manager.get_data(product_key))
        #     ioc.cache_manager.expire(product_key, 600)

        #     return jsonify(cached_data), 200

        # NO CACHE:
        else:
            product = Product.get_by_id(identifier)

            if product is None:
                return jsonify(error_message=f"Product ID {identifier} not found"), 404
            elif product is False:
                raise Exception

            # formatted_product = product.format_dict()
            # ioc.cache_manager.store_data(product_key, json.dumps(formatted_product), 600)

            return product.format_dict(), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting product ID {identifier}: {error}")

@app.route("/products", methods=['POST'])
def add_product():
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_admin(token)

        if validation_result is not True:
            return validation_result

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        new_product = Product(name=name, price=price, entry_date=entry_date, stock=stock)
        result = new_product.add()

        if result is False:
            return jsonify(error_message=f"Error inserting product into the database"), 500

        # CHECK AND INVALIDATE 'ALL' CACHE:
        # all_key = ioc.cache_manager.generate_key("product", "all")

        # if ioc.cache_manager.check_key(all_key)[0]:
        #     delete_cache = ioc.cache_manager.delete_data(all_key)
        #     print("Cache invalidated successfully:", delete_cache)
        # else:
        #     print("No cache to invalidate")

        return jsonify(message=f"Product '{new_product.name}' added successfully"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error inserting product: {error}"), 500


@app.route("/products/<identifier>", methods=["PATCH"])
def update_product(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_admin(token)

        if validation_result is not True:
            return validation_result

        product = Product.get_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404
        elif product is False:
            raise Exception

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        result = product.update(name=name, price=price, entry_date=entry_date, stock=stock)

        if result is False:
            return jsonify(error_message=f"Error updating product ID {identifier}"), 500

        # # SINGLE PRODUCT CACHE:
        # product_key = ioc.cache_manager.generate_key("product", identifier)
        # key_check = ioc.cache_manager.check_key(product_key)

        # if key_check[0]:
        #     delete_cache = ioc.cache_manager.delete_data(product_key)
        #     print("Cache invalidated successfully:", delete_cache)
        # else:
        #     print("No cache to invalidate")

        # # CHECK AND INVALIDATE 'ALL' CACHE:
        # all_key = ioc.cache_manager.generate_key("product", "all")
        # all_check = ioc.cache_manager.check_key(all_key)

        # if all_check[0]:
        #     delete_cache = ioc.cache_manager.delete_data(all_key)
        #     print("Cache invalidated successfully:", delete_cache)
        # else:
        #     print("No cache to invalidate")

        return jsonify(message=f"Product ID {identifier} updated successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating product ID {identifier}: {error}"), 500


@app.route("/products/<identifier>", methods=["DELETE"])
def delete_product(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_admin(token)

        if validation_result is not True:
            return validation_result

        product = Product.get_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404
        elif product is False:
            raise Exception

        result = product.delete()

        if result is False:
            return jsonify(error_message=f"Error deleting product ID {identifier} from the database"), 500

        # # SINGLE PRODUCT CACHE:
        # product_key = ioc.cache_manager.generate_key("product", identifier)
        # key_check = ioc.cache_manager.check_key(product_key)

        # if key_check[0]:
        #     delete_cache = ioc.cache_manager.delete_data(product_key)
        #     print("Cache invalidated successfully:", delete_cache)
        # else:
        #     print("No cache to invalidate")

        # # CHECK AND INVALIDATE 'ALL' CACHE:
        # all_key = ioc.cache_manager.generate_key("product", "all")
        # all_check = ioc.cache_manager.check_key(all_key)

        # if all_check[0]:
        #     delete_cache = ioc.cache_manager.delete_data(all_key)
        #     print("Cache invalidated successfully:", delete_cache)
        # else:
        #     print("No cache to invalidate")

        return jsonify(message=f"Product ID {identifier} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting product ID {identifier}: {error}"), 500

# ------------------- PRODUCTS end -------------------


# ------------------- INVOICES start -------------------
@app.route("/me/<identifier>/invoices", methods=["GET"])
def get_my_invoices(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result, result = validate_same_user_or_admin(token, identifier)

        if validation_result is not True:
            return validation_result

        invoices = Invoice.get_all_by_user_id(result)

        if invoices is None:
            return jsonify(error_message="No invoices found"), 404
        elif invoices is False:
            raise Exception

        return invoices, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's invoices (user ID: {identifier}): {error}"), 500


@app.route("/invoices/<identifier>", methods=["GET"])
def get_invoice_by_id(identifier):
    try:
        token = request.headers.get("Authorization")
        invoice = Invoice.get_by_id(identifier)

        if invoice is None:
            return jsonify(error_message=f"Invoice ID {identifier} not found"), 404
        if invoice is False:
            raise Exception

        validation_result = validate_same_user_or_admin(token, invoice.user_id)[0]

        if validation_result is not True:
            return validation_result

        return invoice.format_dict(), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting invoice ID {identifier}: {error}")

# ------------------- INVOICES end -------------------


# ------------------- SHOP start -------------------
@app.route("/shop", methods=["POST"])
def make_purchase():
    try:
        token = request.headers.get("Authorization")
        validation_result, decoded = validate_user(token)

        if validation_result is not True:
            return validation_result, decoded

        # Data retrieval:
        data = request.get_json()
        user_id = decoded['id']
        purchase_date = data.get('purchase_date')
        invoice_products = data.get('invoice_products') # lista de diccionarios

        if purchase_date is None:
            purchase_date = date.today()

        result, status = Transaction().purchase(user_id, purchase_date, invoice_products)

        if result is not True:
            return jsonify(error_message=result), status

        # # SINGLE PRODUCT CACHE:
        # for product in invoice_products:
        #     product_key = ioc.cache_manager.generate_key("product", product["product_id"])
        #     key_check = ioc.cache_manager.check_key(product_key)

        #     if key_check[0]:
        #         delete_cache = ioc.cache_manager.delete_data(product_key)
        #         print("Cache invalidated successfully:", delete_cache)
        #     else:
        #         print("No cache to invalidate")

        # # CHECK AND INVALIDATE 'ALL' CACHE:
        # all_key = ioc.cache_manager.generate_key("product", "all")
        # all_check = ioc.cache_manager.check_key(all_key)

        # if all_check[0]:
        #     delete_cache = ioc.cache_manager.delete_data(all_key)
        #     print("Cache invalidated successfully:", delete_cache)
        # else:
        #     print("No cache to invalidate")

        return jsonify(message="Purchase successful"), status

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error making purchase: {error}"), 500


@app.route("/shop/my-cart/<identifier>", methods=["GET"])
def get_my_cart(identifier):
    pass


@app.route("/shop/carts/<identifier>", methods=["GET"])
def get_all_carts(identifier):
    pass

# ------------------- SHOP end -------------------


if __name__ == "__main__":
    app.run(host='localhost', port=7000, debug=True)