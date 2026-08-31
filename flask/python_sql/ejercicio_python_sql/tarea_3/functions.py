
def format_users(user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "username":user_record[3],
            "password": user_record[4],
            "date_of_birth": user_record[5],
            "status": user_record[6]
        }


def format_cars(car_record):
        return {
            "id": car_record[0],
            "license_plate": car_record[1],
            "brand": car_record[2],
            "model":car_record[3],
            "year": car_record[4],
            "status": car_record[5]
        }


def format_rentals(rental_record):
        return {
            "id": rental_record[0],
            "car_id": rental_record[1],
            "user_id": rental_record[2],
            "rental_date": rental_record[3],
            "status": rental_record[4],
            "return_date": rental_record[5]
        }