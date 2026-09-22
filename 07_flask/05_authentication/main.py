from ioc_container import ioc
from validations import validate_if_admin, validate_if_same_user_or_admin
from functions import generate_fake_ip
from flask import Flask, request, jsonify
from datetime import date, datetime, timezone

app = Flask("user-service")

# Cómo hago para que solo pueda haber un 'Administrator'? Chequeo el registro de roles como si fuera una lista?

@app.route("/liveness", methods=["GET"])
def liveness():
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        return "<p>Hello, World!</p>", 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error testing liveness: {error}"), 500


@app.route("/refresh-token", methods=["POST"])
def refresh_token():
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify(error_message="Invalid token"), 401

        test_token = token.replace("Bearer ","")
        decoded = ioc.jwt_manager.decode(test_token)

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


# ------------------- start USERS: -------------------
@app.route("/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return jsonify(error_message="Invalid credentials"), 400
        
        hashed_password = ioc.ph.hash(password)

        result = ioc.users_repo.insert(username, hashed_password)

        if result is None:
            return jsonify(error_message="Error inserting user into the database"), 500

        user_id = result
        access_token = ioc.jwt_manager.encode(user_id, "access")

        if access_token is None:
            return jsonify(error_message="Error encoding token"), 401
        
        return jsonify(access_token=access_token), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error registering user: {error}"), 500


@app.route("/login", methods=['POST']) # Por qué esto es un POST y no un GET? Qué estoy creando?
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return jsonify(error_message="Invalid credentials"), 400
        
        user = ioc.users_repo.get_user_by_username(username)

        if user is None:
            return jsonify(error_message="User not found"), 404

        stored_hash = user[2]

        if not ioc.ph.verify(stored_hash, password):
            return jsonify(error_message="Invalid credentials"), 400

        user_id = user[0]
        fake_ip = generate_fake_ip()
        access_token = ioc.jwt_manager.encode(user_id, "access")

        if access_token is None:
            ioc.login_repo.register_login(user_id, now, fake_ip, "failed")
            return jsonify(error_message="Error encoding access token"), 401
        # Hacemos un login validation?

        now = datetime.now(tz=timezone.utc)
        ioc.login_repo.register_login(user_id, now, fake_ip, "successful")

        return jsonify(access_token=access_token), 200

    except Exception as error:
        ioc.login_repo.register_login(user_id, now, fake_ip, "failed")
        print(error)
        return jsonify(error_message=f"Error logging in: {error}"), 500


@app.route("/login-history", methods=["GET"])
def get_login_history():
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        login_history = ioc.login_repo.get_history()

        if login_history is None:
            return jsonify(error_message="Error getting login history from the database"), 500

        return login_history, 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting login history: {error}"), 500


@app.route("/me/<identifier>", methods=["GET"])
def me(identifier):
    try:
        token = request.headers.get('Authorization')
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        user = ioc.users_repo.get_user_by_id(identifier)
        username = user[1]
        role = user[3]

        return jsonify(id=user_id, username=username, role=role), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error accessing user profile: {error}"), 500


@app.route("/me/<identifier>/invoices", methods=["GET"])        # Después implementar filters
def me_invoices(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        invoices = ioc.invoices_repo.get_invoices(user_id)

        if invoices is None:
            return jsonify(message=f"User ID {user_id} has no invoices"), 404

        return jsonify(invoices), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting user's invoices: {error}"), 500


@app.route("/users/<identifier>", methods=["PATCH"])
def update_user(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        user_id = result
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        result = ioc.users_repo.update(user_id, username=username, password=password)

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

# ------------------- end USERS: -------------------

# ------------------- start CONTACTS (EXTRA): -------------------
@app.route("/contacts/<identifier>", methods=["POST"])
def insert_contact(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        new_contact_user_id = ioc.contacts_repo.insert(name, identifier, phone, email)

        if new_contact_user_id is None:
            return jsonify(error_message=f"Error inserting contact into the database"), 500

        return jsonify(message=f"Contact created successfully for user ID {identifier}"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error creating contact for user ID {identifier}: {error}"), 500


@app.route("/contacts/<identifier>", methods=["GET"])
def get_contact(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        contact = ioc.contacts_repo.get_contact_by_user_id(identifier)

        if contact is None:
            return jsonify(message=f"Error getting contact for user ID {identifier} from the database"), 500

        return jsonify(contact), 202

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting contact for user ID {identifier}: {error}"), 500

# Debería hacer un endpoint+method para que el Administrator obtenga TODOS los contacts? "/contacts/all"

@app.route("/contacts/<identifier>", methods=["PATCH"])
def update_contact(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        result = ioc.contacts_repo.update(identifier, name, phone, email)

        if result is None:
            return jsonify(error_message=f"Error updating contact for user ID {identifier} in the database"), 500

        return jsonify(message=f"Contact for user ID {identifier} updated successfully"), 202

    except Exception as error:
        print(error)
        return jsonify(f"Error updating contact for user ID {identifier}: {error}"), 500


@app.route("/contacts/<identifier>", methods=["DELETE"])
def delete_contact(identifier):
    try:
        token = request.headers.get("Authorization")
        validation, result = validate_if_same_user_or_admin(token, identifier)

        if validation is not True:
            return result

        result = ioc.contacts_repo.delete(identifier)

        if result is None:
            return jsonify(error_message=f"Error deleting contact for user ID {identifier} from the database"), 500

        return jsonify(message=f"Contact for user ID {identifier} deleted successfully"), 202

    except Exception as error:
        print(error)
        return jsonify(f"Error deleting contact for user ID {identifier}: {error}"), 500

# ------------------- end CONTACTS (EXTRA): -------------------

# ------------------- start PRODUCTS: -------------------
@app.route("/products", methods=["POST"])
def insert_product():
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

        result_name = ioc.products_repo.insert(name, price, entry_date, stock) 

        if result_name is None:
            return jsonify(error_message=f"Error inserting product into the database"), 500

        return jsonify(message=f"Product '{result_name}' inserted successfully"), 201

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error inserting product: {error}"), 500


@app.route("/products/<identifier>", methods=["GET"])
def get_product(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        product = ioc.products_repo.get_product_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404

        return jsonify(id=identifier, name=product[1], price=product[2], entry_date=product[3], stock=product[4]), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting product ID {identifier}: {error}"), 500


@app.route("/products/<identifier>", methods=["PATCH"])
def update_product(identifier):
    try:
        token = request.headers.get("Authorization")
        validation_result = validate_if_admin(token)

        if validation_result is not True:
            return validation_result

        product = ioc.products_repo.get_product_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404

        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        entry_date = data.get('entry_date')
        stock = data.get('stock')

        result = ioc.products_repo.update(identifier, name=name, price=price, entry_date=entry_date, stock=stock)

        if result is None:
            return jsonify(error_message=f"Error updating product ID {identifier}"), 500

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

        product = ioc.products_repo.get_product_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Product ID {identifier} not found"), 404

        result = ioc.products_repo.delete(identifier)

        if result is None:
            return jsonify(error_message=f"Error deleting product ID {identifier} from the database"), 500

        return jsonify(message=f"Product ID {identifier} deleted successfully"), 200

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting product ID {identifier}: {error}"), 500

# ------------------- end PRODUCTS: -------------------

# ------------------- start STORE: -------------------
@app.route("/store", methods=["POST"])
def make_purchase():
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify(error_message="Invalid token"), 401

        test_token = token.replace("Bearer ","")
        decoded = ioc.jwt_manager.decode(test_token)

        if decoded is None:
            return jsonify(error_message="Error decoding token"), 401

        # Data retrieval:
        data = request.get_json()
        user_id = decoded['id']
        purchase_date = data.get('purchase_date')
        invoice_products = data.get('invoice_products') # lista de diccionarios

        if purchase_date is None:
            purchase_date = date.today()

        result, status = ioc.transactions_repo.purchase(user_id, purchase_date, invoice_products)

        if result is not True:
            return jsonify(error_message=result), status

        return jsonify(message="Purchase successful"), status

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error making purchase: {error}"), 500


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)