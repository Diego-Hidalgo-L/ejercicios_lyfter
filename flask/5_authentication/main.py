from ioc_container import IocContainer
from flask import Flask, request, Response, jsonify

app = Flask("user-service")
ioc = IocContainer()

# MENSAJES JSONIFY y RESPONSES:
# Van aquí, no en el repositorio.

@app.route("/liveness", methods=["GET"])
def liveness():
    return "<p>Hello, World!</p>"


# ------------------- start USERS: -------------------
@app.route("/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')

        if username is None or password is None:
            return jsonify(error_message="Invalid credentials"), 403
        
        hashed_password = ioc.ph.hash(password)
        result = ioc.users_repo.insert(username, hashed_password, role)

        if result is None:
            return jsonify(error_message="Error registering user"), 403

        user_id = result[0]     # 'result' es un tupla - esto devuelve su primer índice (id)
        token = ioc.jwt_manager.encode({'id':user_id})

        if token is None:
            return jsonify(error_message="Error encoding token"), 403
        
        return jsonify(token=token)

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error registering user: {error}"), 400


@app.route("/login", methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username is None or password is None:
            return jsonify(error_message="Invalid credentials"), 403
        
        user = ioc.users_repo.get_user_by_username(username)

        if user is None:
            return jsonify(error_message="Invalid credentials"), 403

        stored_hash = user[2]

        if not ioc.ph.verify(stored_hash, password):
            return jsonify(error_message="Invalid credentials"), 403

        user_id = user[0]
        token = ioc.jwt_manager.encode({'id':user_id})

        if token is None:
            return jsonify(error_message="Error encoding token"), 403
    
        return jsonify(token=token)

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error logging in: {error}"), 400


@app.route("/me", methods=["GET"])
def me():
    try:
        token = request.headers.get('Authorization')

        if token is None:
            return jsonify(error_message="Empty token"), 403
        
        test_token = token.replace("Bearer ","")
        print(test_token)
        decoded = ioc.jwt_manager.decode(test_token)

        if decoded is None:
            return jsonify(error_message="Error decoding token"), 403

        user_id = decoded['id']
        user = ioc.users_repo.get_user_by_id(user_id)

        if user is None:
            return jsonify(error_message="Invalid credentials"), 403

        return jsonify(id=user_id, username=user[1])

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error accessing user profile: {error}"), 400


@app.route("/users/<identifier>", methods=["PATCH"]) # Tiene sentido pasar el ID como un path parameter? 
def update_user(identifier):                         # Si estoy logged ya debería tener acceso a mi ID y solo debería poder eliminar mi propio user.
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify(error_message="Invalid credentials"), 403

        user = ioc.users_repo.get_user_by_id(identifier)

        if user is None:
            return jsonify(error_message="Invalid credentials"), 403 

        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        
        result = ioc.users_repo.update(identifier, username=username, password=password, role=role)

        if result is None:
            return jsonify(error_message=f"Error updating user ID {identifier}: {error}"), 403
        
        return jsonify(message=f"User ID {identifier} updated successfully")

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user ID {identifier}: {error}"), 403

@app.route("/users/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify(error_message="Invalid credentials"), 403

        user = ioc.users_repo.get_user_by_id(identifier)

        if user is None:
            return jsonify(error_message="Invalid credentials"), 403

        result = ioc.users_repo.delete(identifier)

        if result is None:
            jsonify(error_message=f"Error deleting user ID {identifier}: {error}"), 403

        return jsonify(message=f"User ID {identifier} deleted successfully")

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error deleting user ID {identifier}: {error}"), 403

# ------------------- end USERS: -------------------

# ------------------- start PRODUCTS: -------------------
@app.route("/products/<identifier>", methods=["GET"])
def get_product(identifier):
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify(error_message="Invalid credentials"), 403

        product = ioc.products_repo.get_product_by_id(identifier)

        if product is None:
            return jsonify(error_message=f"Error getting product ID {identifier}: {error}"), 403

        return jsonify(id=identifier, name=product[1], price=product[2], entry_date=product[3], stock=product[4])

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error getting product ID {identifier}: {error}"), 403




if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)