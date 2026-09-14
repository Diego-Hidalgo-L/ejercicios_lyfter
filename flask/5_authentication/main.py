from ioc_container import IocContainer
from flask import Flask, request, Response, jsonify

app = Flask("user-service")
ioc = IocContainer()


@app.route("/liveness", methods=["GET"])
def liveness():
    return "<p>Hello, World!</p>"


@app.route('/register', methods=['POST'])
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


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  # data is empty
        username = data.get('username')
        password = data.get('password')
        
        if username is None or password is None:
            return Response(status=400)
        
        user = ioc.users_repo.get_user(username)

        if user is None:
            return Response(status=403)

        stored_hash = user[2]

        if not ioc.ph.verify(stored_hash, password):
            return Response(status=403)

        user_id = user[0]
        token = ioc.jwt_manager.encode({'id':user_id})
    
        return jsonify(token=token)

    except Exception as error:
        print(error)


@app.route('/me', methods=["GET"])
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


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)