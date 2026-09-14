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
            return Response(status=400)
        
        hashed_password = ioc.ph.hash(password)

        result = ioc.users_repo.insert(username, hashed_password, role)
        user_id = result[0]     # 'result' es un tupla - esto devuelve su primer índice (id)

        token = ioc.jwt_manager.encode({'id':user_id})
        
        return jsonify(token=token)

    except Exception as error:
            print(error)


@app.route("/login", methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username is None or password is None:
            return Response(status=400)
        
        user = ioc.users_repo.get_user_by_username(username)

        if user is None:
            return Response(status=403)

        # stored_hash = user[2]

        # if not ioc.ph.verify(stored_hash, password):
        #     return Response(status=403)

        user_id = user[0]
        token = ioc.jwt_manager.encode({'id':user_id})
    
        return jsonify(token=token)

    except Exception as error:
        print(error)


@app.route("/me", methods=["GET"])
def me():
    try:
        token = request.headers.get('Authorization')

        if token is None:
            return Response(status=403)
        
        test = token.replace("Bearer ","")
        print(test)
        decoded = ioc.jwt_manager.decode(test)

        if decoded is None:
            return Response(status=403)

        user_id = decoded['id']
        user = ioc.users_repo.get_user_by_id(user_id)

        return jsonify(id=user_id, username=user[1])

    except Exception as error:
        print(error)


@app.route("/users/<identifier>", methods=["PATCH"]) # Tiene sentido pasar el ID como un path parameter? 
def update_user(identifier):                        # Si estoy loggeado ya debería tener acceso a mi ID y solo debería poder eliminar mi propio user.
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return jsonify(error_message="Invalid token"), 403

        user = ioc.users_repo.get_user_by_id(identifier)

        if user is None:
            return jsonify(error_message="Invalid user"), 403 

        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        
        ioc.users_repo.update(identifier, username=username, password=password, role=role)

        return jsonify(message=f"User ID {identifier} updated successfully")

    except Exception as error:
        print(error)
        return jsonify(error_message=f"Error updating user ID {identifier}: {error}"), 403

@app.route("/users/<identifier>", methods=["DELETE"])
def delete_user(identifier):
    try:
        token = request.headers.get("Authorization")

        if token is None:
            return Response(status=403)

        user = ioc.users_repo.get_user_by_id(identifier)

        if user is None:
            return Response(status=403)

        ioc.users_repo.delete(identifier)

        return

    except Exception as error:
        print(error)

# ------------------- end USERS: -------------------

# ------------------- start PRODUCTS: -------------------
@app.route("/products", methods=["GET"])
def get_product():
    pass




if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)