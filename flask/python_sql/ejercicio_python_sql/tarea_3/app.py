from flask import Flask, request, jsonify
from db import db_manager
from py_functions import format_users, format_cars, format_rentals

app = Flask(__name__)

# USERS:
@app.route("/users")
def get_users():
    try:
        filters = request.args
        valid_columns = ["id", "full_name", "email", "username", "password", "date_of_birth", "status"]
        filter_columns = []
        filter_values = []

        if filters:

            for column, value in filters.items():
                column = column.strip().lower()

                if column in valid_columns:
                    filter_columns.append(f"{column} = %s")
                    filter_values.append(value)
                else:
                    return jsonify(error_message=f"Invalid filter: {column}"), 400

            where_clause = " AND ".join(filter_columns)
            query = f"SELECT * FROM users WHERE {where_clause};" 

        else:
            query = "SELECT * FROM users;"

        results = db_manager.fetchall(query, *filter_values)
        return [format_users(user) for user in results]

    except Exception as error:
        return jsonify(error_message=f"Error getting users {error}"), 500


@app.route("/users", methods=["POST"])
def add_user():
    try:
        request_body = request.json
        values = (
            request_body.get("full_name"),
            request_body.get("email"),
            request_body.get("username"),
            request_body.get("password"),
            request_body.get("date_of_birth"),
            request_body.get("status")
        )

        # No valido si el email o el username ya existen, porque tiene el constraint de UNIQUE en la DB.

        query = """
            INSERT INTO users (full_name, email, username, password, date_of_birth, status)
            VALUES (%s, %s, %s, %s, %s, %s);
            """

        execute_result = db_manager.execute_query(query, *values)

        if not execute_result:
            raise Exception("Error executing query")
        
        db_manager.commit()
        return jsonify(message="User added successfully!"), 201

    except Exception as error:
        db_manager.rollback()
        return jsonify(error_message=f"Error adding user to database: {error}"), 400


@app.route("/users/<identifier>", methods=["PATCH"])


# CARS:
@app.route("/cars")
def get_cars():
    filters = request.args
    valid_columns = ["id", "license_plate", "brand", "model", "year", "status"]
    filter_columns = []
    filter_values = []

    if filters:

        for column, value in filters.items():
            column = column.strip().lower()

            if column in valid_columns:
                filter_columns.append(f"{column} = %s")
                filter_values.append(value)
            else:
                return jsonify(error_message=f"Invalid filter: {column}"), 400

        where_clause = " AND ".join(filter_columns)
        query = f"SELECT * FROM cars WHERE {where_clause};" 

    else:
        query = "SELECT * FROM cars;"

    results = db_manager.fetchall(query, *filter_values)
    return [format_cars(car) for car in results]


@app.route("/cars", methods=["POST"])
def add_car():
    try:
        request_body = request.json
        values = (
            request_body.get("license_plate"),
            request_body.get("brand"),
            request_body.get("model"),
            request_body.get("year"),
            request_body.get("status")
        )

        query = """
            INSERT INTO cars (license_plate, brand, model, year, status)
            VALUES (%s, %s, %s, %s, %s);
            """

        execute_result = db_manager.execute_query(query, *values)

        if not execute_result:
            raise Exception("Error executing query")
        
        db_manager.commit()
        return jsonify(message="Car added successfully"), 201

    except Exception as error:
        db_manager.rollback()
        return jsonify(error_message=f"Error adding car to database: {error}"), 400


@app.route("/cars/<identifier>", methods=["PATCH"])


# RENTALS:
@app.route("/rentals")
def get_rentals():
    filters = request.args
    valid_columns = ["id", "car_id", "user_id", "rental_date", "status", "return_date"]
    filter_columns = []
    filter_values = []

    if filters:

        for column, value in filters.items():
            column = column.strip().lower()

            if column in valid_columns:
                filter_columns.append(f"{column} = %s")
                filter_values.append(value)
            else:
                return jsonify(error_message=f"Invalid filter: {column}"), 400

        where_clause = " AND ".join(filter_columns)
        query = f"SELECT * FROM rentals WHERE {where_clause};" 

    else:
        query = "SELECT * FROM rentals;"

    results = db_manager.fetchall(query, *filter_values)
    return [format_rentals(rental) for rental in results]


@app.route("/rentals", methods=["POST"])
def add_rental():
    try:
        request_body = request.json
        user_id = request_body.get("user_id")
        car_id = request_body.get("car_id")
        rental_date = request_body.get("rental_date")
        columns = (user_id, car_id, rental_date)

        query = "SELECT add_rental(%s, %s, %s)"

        db_manager.execute_query(query, *columns)
        db_manager.commit()

        return jsonify(message="Rental added successfully"), 201

    except Exception as error:
        db_manager.rollback()
        return jsonify(error_message=f"Error adding rental: {error}"), 400


@app.route("/rentals/<identifier>", methods=["PATCH"])
def patch_rentals():
    pass


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)