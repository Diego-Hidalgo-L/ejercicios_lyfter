from ioc_container import ioc
from db import User, Product
from validations import validate_if_admin, validate_if_same_user_or_admin
from functions import generate_fake_ip

from flask import Flask, request, jsonify
from argon2.exceptions import VerifyMismatchError
from datetime import date, datetime, timezone
import json


app = Flask("e-commerce")


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
            return jsonify(error_message="Invalid credentials"), 400                                                ######

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


@app.route("/me/<identifier>", methods=["GET"])
def me(identifier):
    try:
        token = request.headers.get('Authorization')
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        user = User.get_by_id(identifier)
        username = user.id
        role = user.role

        return jsonify(id=user_id, username=username, role=role), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error accessing user profile: {error}"), 500


@app.route("/users/<identifier>", methods=["PATCH"])
def update_user(identifier):
    try:
        token = request.headers.get("Authorization")
        user = User.get_by_id(identifier)

        if not user:
            return jsonify(error_message=f"User ID {identifier} not found"), 404
        
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

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
        return jsonify(error_message=f"Error updating user ID {user_id}: {error}"), 500


@app.route("/users/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        delete_result = ioc.users_repo.delete(user_id)

        if delete_result is None:
            return jsonify(error_message=f"Error deleting user ID {user_id} from the database"), 500

        return jsonify(message=f"User ID {user_id} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user ID {user_id}: {error}"), 500

# ------------------- USERS end -------------------


# ------------------- SHOPPING CART start -------------------
@app.route("/shop/my-cart/<identifier>", methods=["GET"])
def get_my_cart(identifier):
    pass


@app.route("/shop/carts/<identifier>", methods=["GET"])
def get_all_carts(identifier):
    pass

# ------------------- SHOPPING CART end -------------------

if __name__ == "__main__":
    app.run(host='localhost', port=7000, debug=True)