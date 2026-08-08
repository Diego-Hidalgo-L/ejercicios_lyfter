from flask import Flask, request, jsonify

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
    if not comment_content:
        return jsonify(message="no empty comments allowed"), 400

    comments_list.append(comment_content)
    return comments_list


if __name__ == "__main__":
    app.run(host='localhost', debug=True)