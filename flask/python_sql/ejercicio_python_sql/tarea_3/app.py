from flask import Flask, request
from repositories import users_repo, cars_repo, rentals_repo

app = Flask(__name__)

# USERS:
@app.route("/users")
def get_users():
    filters = request.args
    return users_repo.get_users(filters)


@app.route("/users", methods=["POST"])
def add_user():
    request_body = request.json
    return users_repo.add_user(request_body)


@app.route("/users/<identifier>", methods=["PATCH"])
def update_user_status(identifier):
    request_body = request.json
    return users_repo.update_user_status(identifier, request_body)


# CARS:
@app.route("/cars")
def get_cars():
    filters = request.args
    return cars_repo.get_cars(filters)


@app.route("/cars", methods=["POST"])
def add_car():
    request_body = request.json
    return cars_repo.add_car(request_body)


@app.route("/cars/<identifier>", methods=["PATCH"])
def update_car_status(identifier):
    request_body = request.json
    return cars_repo.update_car_status(identifier, request_body)

# RENTALS:
@app.route("/rentals")
def get_rentals():
    filters = request.args
    return rentals_repo.get_rentals(filters)


@app.route("/rentals", methods=["POST"])
def add_rental():
    request_body = request.json
    return rentals_repo.add_rental(request_body)


@app.route("/rentals/<car_id>", methods=["PATCH"])
def update_rental_status(car_id):
    request_body = request.json
    return rentals_repo.update_rental_status(car_id, request_body)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)