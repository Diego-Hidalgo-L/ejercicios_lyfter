from flask import jsonify
from db import db_manager
from functions import format_users, format_cars, format_rentals
from datetime import date

class UsersRepo:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_users(self, filters):
        try:
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

            results = self.db_manager.fetchall(query, *filter_values)
            return [format_users(user) for user in results]

        except Exception as error:
            return jsonify(error_message=f"Error getting users {error}"), 500

    def add_user(self, request_body):
        try:
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

            execute_result = self.db_manager.execute_query(query, *values)

            if not execute_result:
                raise Exception("Error executing query")
            
            self.db_manager.commit()

            return jsonify(message="User added successfully!"), 201

        except Exception as error:
            self.db_manager.rollback()
            return jsonify(error_message=f"Error adding user to database: {error}"), 400

    def update_user_status(self, identifier, request_body):
        try:
            status = request_body.get("status")
            # Si no viene key "status", el try/except lo atrapará.

            query = """
                UPDATE users
                SET status = %s
                WHERE id = %s;
                """

            execute_result = self.db_manager.execute_query(query, status, identifier)

            if not execute_result:
                raise Exception("Error executing query")
            
            self.db_manager.commit()
            return jsonify(message=f"User {identifier} status updated successfully!")

        except Exception as error:
            self.db_manager.rollback()
            return jsonify(error_message=f"Error updating user status: {error}"), 400


class CarsRepo:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_cars(self, filters):
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

        results = self.db_manager.fetchall(query, *filter_values)
        return [format_cars(car) for car in results]

    def add_car(self, request_body):
        try:
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

            execute_result = self.db_manager.execute_query(query, *values)

            if not execute_result:
                raise Exception("Error executing query")
            
            self.db_manager.commit()
            return jsonify(message="Car added successfully"), 201

        except Exception as error:
            self.db_manager.rollback()
            return jsonify(error_message=f"Error adding car to database: {error}"), 400

    def update_car_status(self, identifier, request_body):
        try:
            status = request_body.get("status")

            query = """
                UPDATE cars
                SET status = %s
                WHERE id = %s;
                """

            execute_result = self.db_manager.execute_query(query, status, identifier)

            if not execute_result:
                raise Exception("Error executing query")
            
            self.db_manager.commit()
            return jsonify(message=f"Car {identifier} status updated successfully!"), 200

        except Exception as error:
            self.db_manager.rollback()
            return jsonify(error_message=f"Error updating car status: {error}"), 400


class RentalsRepo:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_rentals(self, filters):
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

        results = self.db_manager.fetchall(query, *filter_values)
        return [format_rentals(rental) for rental in results]

    def add_rental(self, request_body):
        try:
            user_id = request_body.get("user_id")
            car_id = request_body.get("car_id")
            rental_date = request_body.get("rental_date")
            columns = (user_id, car_id, rental_date)

            query = "SELECT add_rental(%s, %s, %s)"

            execute_result = self.db_manager.execute_query(query, *columns)

            if not execute_result:
                raise Exception("Error executing query")

            self.db_manager.commit()
            return jsonify(message="Rental added successfully"), 201

        except Exception as error:
            self.db_manager.rollback()
            return jsonify(error_message=f"Error adding rental: {error}"), 400

    def update_rental_status(self, car_id, request_body):
        try:
            status = request_body.get("status")
            return_date = request_body.get("return_date")

            if status == "returned" and not return_date:
                return_date = date.today()

            results = self.db_manager.fetchall("SELECT * FROM rentals WHERE car_id = %s AND status = 'ongoing';", car_id)

            # Este diseño no permite cambiar el status de 'returned' a 'ongoing', lo cual tiene cierto sentido por seguridad.
            # Pero dejo los comentarios abajo por si fuera necesario modificar esa lógica.

            if not results:
                return jsonify(error_message=f"There are no ongoing rentals for car ID {car_id}"), 400

            # if status == "returned":
            query = """
                UPDATE rentals
                SET status = %s, return_date = %s
                WHERE car_id = %s;

                UPDATE cars
                SET status = 'available'
                WHERE id = %s;
                """
            # elif status == "ongoing":
            #     query = """
            #         UPDATE rentals
            #         SET status = %s, return_date = null
            #         WHERE car_id = %s;

            #         UPDATE cars
            #         SET status = 'rental ongoing'
            #         WHERE id = %s;
            #         """

            execute_result = self.db_manager.execute_query(query, status, return_date, car_id, car_id)

            if not execute_result:
                raise Exception("Error executing query")

            self.db_manager.commit()
            return jsonify(message=f"Rental status for car ID {car_id} updated successfully!"), 200

        except Exception as error:
            self.db_manager.rollback()
            return jsonify(error_message=f"Error updating rental status: {error}"), 400


# CLASS INSTANCES:
users_repo = UsersRepo(db_manager)
cars_repo = CarsRepo(db_manager)
rentals_repo = RentalsRepo(db_manager)