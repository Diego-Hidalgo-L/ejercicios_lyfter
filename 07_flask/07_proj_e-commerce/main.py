from ioc_container import ioc
from db import User, Product
from validations import validate_if_admin, validate_if_same_user_or_admin, validate_user
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

        if result is None:
            return jsonify(error_message="Error inserting user into the database"), 500

        user_id = result.id
        access_token = ioc.jwt_manager.encode(user_id, "access")
        refresh_token = ioc.jwt_manager.encode(user_id, "refresh")

        if access_token is None:
            return jsonify(error_message="Error encoding token"), 401

        elif refresh_token is None:
            return jsonify(error_message="Error encoding refresh token"), 401
        
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200

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
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        users = User.get_all()

        return jsonify(users), 200
        
    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting all users: {error}"), 500


@app.route("/me/<identifier>", methods=["GET"])
def me(identifier):
    try:
        token = request.headers.get('Authorization')
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        user = User.get_by_id(identifier)
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
        validation, result = validate_if_same_user_or_admin(token, identifier)

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

        if result is None:
            return jsonify(error_message=f"Error updating user ID {user_id}"), 403
        
        return jsonify(message=f"User ID {user_id} updated successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user ID {identifier}: {error}"), 500


@app.route("/users/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user = User.get_by_id(identifier)

        if not user:
            return jsonify(error_message=f"User ID {identifier} not found"), 404

        user_id = result
        delete_result = user.delete()

        if delete_result is None:
            return jsonify(error_message=f"Error deleting user ID {user_id} from the database"), 500

        return jsonify(message=f"User ID {user_id} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user ID {identifier}: {error}"), 500

# ------------------- USERS end -------------------


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
                return jsonify(error_message="Error getting all products"), 500

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

            # formatted_product = product.format_dict()
            # ioc.cache_manager.store_data(product_key, json.dumps(formatted_product), 600)

            return jsonify(id=identifier, name=product.name, price=product.price, entry_date=product.entry_date, stock=product.stock), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting product ID {identifier}: {error}")

@app.route("/products", methods=['POST'])
def add_product():
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        new_product = Product(name=name, price=price, entry_date=entry_date, stock=stock)
        result = new_product.add()

        if result is None:
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
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        product = Product.get_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        result = product.update(name=name, price=price, entry_date=entry_date, stock=stock)

        if result is None:
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
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        product = Product.get_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404

        result = product.delete()

        if result is None:
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