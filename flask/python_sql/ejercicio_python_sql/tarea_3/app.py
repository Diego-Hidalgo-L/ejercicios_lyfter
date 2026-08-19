from flask import Flask, request, jsonify
from db import db_manager
from functions import format_user

app = Flask(__name__)

# USERS:
@app.route("/users")
def get_users():
    filters = request.args
    allowed_columns = ["id", "full_name", "email", "username", "password", "date_of_birth", "status"]
    filter_columns = []
    filter_values = []

    if filters:
        for column, value in filters.items():
            column = column.strip().lower()
            
            if column in allowed_columns:
                filter_columns.append(f"{column} = %s")
                filter_values.append(value)
            else:
                return jsonify(error_message=f"Invalid filter: {column}"), 400

        where_clause = " AND ".join(filter_columns)
        query = f""" 
            SELECT *
            FROM users
            WHERE {where_clause};
            """ # Estos queries los vamos a cambiar por objetos de los repositories.

    else:
        query = "SELECT * FROM users;"

    results = db_manager.fetchall(query, *filter_values)  
    
    return [format_user(user) for user in results]


@app.route("/users", methods=["POST"])


@app.route("/users/<identifier>", methods=["PATCH"])


# CARS:
@app.route("/cars")


@app.route("/cars", methods=["POST"])


@app.route("/cars/<identifier>", methods=["PATCH"])


# RENTALS:
@app.route("/rentals")


@app.route("/rentals", methods=["POST"])


@app.route("/rentals/<identifier>", methods=["PATCH"])
def patch_rentals():
    pass


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)