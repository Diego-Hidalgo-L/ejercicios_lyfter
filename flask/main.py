from flask import Flask, Response, json, request, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    print("Hola! Mi primera ruta en mi primer API.")
    return "<h1>Hello, World!</h1>"


@app.route("/information")
def information():
    return {
        'year': 2026,
        'description': "Esto es un endpoint secundario"
    }


@app.route("/goodbye")
def goodbye():
    print("Adiós! Mi segunda ruta en mi primer API.")
    return "<h1>Bye, World!</h1>"


# Path parameters:
@app.route("/user/<username>/<color>")
def profile(username, color):
    return f"{color} {username}'s profile."


@app.route("/shop/<category>/<subcategory>/all")
def products_subcategory(category, subcategory):
    return f"Shopping category {category}, {subcategory}"


# Query parameters:
shows_list = [
    {
        "title": "3 Body Problem",
        "genre": "Sci-Fi",
    },
    {
        "title": "Severance",
        "genre": "Thriller",
    },
    {
        "title": "Black Knight",
        "genre": "Sci-Fi",
    },
]

@app.route("/shows")
def shows():
    filtered_shows = shows_list
    genre_filter = request.args.get("genre")
    if genre_filter:
        filtered_shows = list(
            filter(lambda show: show["genre"] == genre_filter, filtered_shows)
        )

    return {"data": filtered_shows}


# Requests con body:
@app.route("/echo", methods=["POST"])
def echo():
    request_body = request.json
    print(f"El nombre del que hizo el request es {request_body.get("name")}")
    return {"request_body": request_body}


# Requests con body en formato de 'form':
comments_list = [
    "Genial video, entendí todo a la perfeccion!",
    "Me encantó el intro jajaja",
]

@app.route("/comment", methods=["POST"])
def post_comment():
    comment_content = request.form.get("comment_content") # .form también viene en formato de diccionario, por eso se puede hacer .get()
    if not comment_content: # podría manejarse otro error para cuando no se incluye este key en el path DEL TODo.
        return jsonify(message="no empty comments allowed"), 400

    comments_list.append(comment_content)
    return comments_list


# Validación:
users_list = [
	{
		"email": "action.bronson@gmail.com",
		"password": "123@a!",
	},
]

@app.route("/register", methods=["POST"])
def register_user():
    try:
        if "email" not in request.json: # Si el request no trae el email, mandamos error.
            raise ValueError("email missing from the body")

        if "password" not in request.json: # Si el request no trae el password, mandamos error.
            raise ValueError("password missing from the body")

        users_list.append(
            {
                "email": request.json["email"],
                "password": request.json["password"],
            }
        )
        return users_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
	    # enviar un mensaje por slack
        return jsonify(message=str(ex)), 500

# Autenticación:
@app.route('/view-token')
def view_token():
	token = request.headers.get('token', '') # Puedo accesar a cualquiera de los headers a través del atributo .headers en formato diccionario.
	return token


# RESPONSES:
@app.route("/hello") # 3ro MEJOR: para retornar responses mucho más ESPECÍFICOS.
def hello():
    response_body = json.dumps({"msg": "Hello World!"}) # dumps: 'dump string' -> convierte el json en un string.
    return Response(response_body, status=200, mimetype="application/json") # Response no convierte nada automáticamente; no hace ninguna suposición.

@app.route("/hello2") # MEJOR: cuando queremos retornar DATOS PRIMITIVOS.
def hello2():
    return {"msg": "Hello, World!"}, 201


from dataclasses import dataclass

@dataclass
class HelloResponse: # Usar objetos para los responses es una buena práctica (estructura definida)
    msg: str

@dataclass
class LoginResponse: # Provee mayor información y orden sobre cada response para cada request diferente.
    msg: str

@dataclass
class RegisterResponse: #Sirve para evitar redundancia (DRY).
    msg: str

@app.route("/hello3") # 2do MEJOR: para retornar datos NO primitivos (como clases.)
def hello3():
    response = HelloResponse("Hello, World!") # Usar objetos para los responses es una buena práctica (estructura definida)
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host='localhost', debug=True)