
class UsersRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_user(self, full_name, email, username, password, date_of_birth, status): # Debería crear validaciones para cada parámetro?
        try:
            self.db_manager.execute_query("""
                INSERT INTO lyfter_car_rental.users
                VALUES (%s, %s, %s, %s, %s, %s);""",
                (full_name, email, username, password, date_of_birth, status)
                )

            print("User entered successfully")
            return True

        except Exception as error:
            print("Error entering new user:", error)
            return False

    def update_status(self, _id, status): # Debería crear una validación para estos parameters también?
        try:
            self.db_manager.execute_query("""
                UPDATE lyfter_car_rental.users
                SET status = %s
                WHERE id = %s""",
                (_id, status)
                )

            print("User status updated successfully")
            return True

        except Exception as error:
            print("Error updating user status:", error)
            return False


class CarsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_car(self, brand, model, year, status):
        try:
            self.db_manager.execute_query("""
                INSERT INTO lyfter_car_rental.cars
                VALUES (%s, %s, %s, %s);""",
                (brand, model, year, status)
                )

            print("Car entered successfully")
            return True
        
        except Exception as error:
            print("Error entering new car:", error)
            return False

    def update_status(self, status, _id): # Debería crear una validación para estos parameters también?
        try:
            self.db_manager.execute_query("""
                UPDATE lyfter_car_rental.cars
                SET status = %s
                WHERE id = %s;""",
                (status, _id)
                )

            print("User status updated successfully")
            return True

        except Exception as error:
            print("Error updating user status:", error)
            return False


class RentalsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_rental(self, car_id, user_id, rental_date, status):
        try:
            self.db_manager.execute_query("""
                INSERT INTO rentals
                VALUES (%s, %s, %s, %s);""",
                (car_id, user_id, rental_date, status)
                )

            print("Rental entered successfully")
            return True

        except Exception as error:
            print("Error entering new rental:", error)
            return False

    def return_rental(self):
        self.db_manager.execute_query("""
            """
            )