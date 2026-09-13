from ioc_container import IocContainer
from flask import Flask, request, Response, jsonify

app = Flask("user-service")
ioc = IocContainer()


@app.route("/liveness", methods=["GET"])
def liveness():
    return "<p>Hello, World!</p>"


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if data.get('username') == None or data.get('password') == None:
        return Response(status=400)
    else:
        result = ioc.users_repo.insert(data.get('username'), data.get('password'))
        user_id = result[0]

        token = ioc.jwt_manager.encode({'id':user_id})
        
        return jsonify(token=token)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if data.get('username') == None or data.get('password') == None:
        return Response(status=400)
    else:
        result = ioc.users_repo.get_user(data.get('username'), data.get('password'))

        if result is None:
            return Response(status=403)
        else:
            user_id = result[0]
            token = ioc.jwt_manager.encode({'id':user_id})
        
            return jsonify(token=token)


@app.route('/me')
def me():
    try:
        token = request.headers.get('Authorization')

        if token is not None:
            test = token.replace("Bearer ","")
            print(test)
            decoded = ioc.jwt_manager.decode(test)

            if decoded is None:
                return Response(status=403)

            user_id = decoded['id']
            user = ioc.users_repo.get_user_by_id(user_id)

            return jsonify(id=user_id, username=user[1])
        else:
            return Response(status=403)
        
    except Exception as e:
        return Response(status=500)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)