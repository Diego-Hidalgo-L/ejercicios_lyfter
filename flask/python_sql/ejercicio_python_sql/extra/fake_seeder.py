from tarea_3.db import db_manager
from faker import Faker
import random
import string

fake = Faker()

def insert_fake_users():
    status_list = ('active', 'deactivated', 'payment pending')

    try:
        for _ in range(200):
            args = (fake.name(), fake.unique.email(), fake.unique.user_name(), fake.password(), fake.date_of_birth(), random.choice(status_list))
            query = """
                INSERT INTO users (full_name, email, username, password, date_of_birth, status)
                VALUES (%s, %s, %s, %s, %s, %s);
                """

            db_manager.execute_query(query, *args)

        db_manager.commit()
        print("Users inserted and committed")

    except Exception as error:
        db_manager.rollback()
        print(f"Error inserting fake users: {error}")


def insert_fake_cars():
    car_models = {
    "Toyota": [
        "Corolla",
        "Camry",
        "RAV4",
        "Prius",
        "Hilux",
        "Land Cruiser"
    ],
    "Honda": [
        "Civic",
        "Accord",
        "CR-V",
        "HR-V",
        "Pilot",
        "Odyssey"
    ],
    "Ford": [
        "Mustang",
        "F-150",
        "Explorer",
        "Escape",
        "Bronco",
        "Ranger"
    ],
    "Chevrolet": [
        "Malibu",
        "Camaro",
        "Corvette",
        "Tahoe",
        "Suburban",
        "Equinox"
    ],
    "Nissan": [
        "Sentra",
        "Altima",
        "Rogue",
        "Pathfinder",
        "Frontier",
        "Versa"
    ],
    "Hyundai": [
        "Elantra",
        "Sonata",
        "Tucson",
        "Santa Fe",
        "Kona",
        "Palisade"
    ],
    "Kia": [
        "Forte",
        "K5",
        "Sportage",
        "Sorento",
        "Telluride",
        "Seltos"
    ],
    "Volkswagen": [
        "Golf",
        "Jetta",
        "Passat",
        "Tiguan",
        "Taos",
        "Atlas"
    ],
    "BMW": [
        "3 Series",
        "5 Series",
        "7 Series",
        "X3",
        "X5",
        "X7"
    ],
    "Mercedes-Benz": [
        "A-Class",
        "C-Class",
        "E-Class",
        "S-Class",
        "GLC",
        "GLE"
    ],
    "Mazda": [
        "Mazda3",
        "Mazda6",
        "CX-3",
        "CX-5",
        "CX-30",
        "CX-90"
    ],
    "Subaru": [
        "Impreza",
        "Legacy",
        "Outback",
        "Forester",
        "Crosstrek",
        "Ascent"
    ]
}
    status_list = ('available', 'rental ongoing', 'rent ineligible')

    try:
        for _ in range(100):
            license_plate = (
                    ''.join(random.choices(string.ascii_uppercase, k=3))
                    + ''.join(random.choices(string.digits, k=3))
                )
            brand = random.choice(list(car_models))
            model = random.choice(car_models[brand])
            year = random.randint(2010, 2026)
            status = random.choice(status_list)
            
            args = (license_plate, brand, model, year, status)
            query = """
                INSERT INTO cars (license_plate, brand, model, year, status)
                VALUES (%s, %s, %s, %s, %s);
                """

            db_manager.execute_query(query, *args)

        db_manager.commit()
        print("Cars inserted and committed")

    except Exception as error:
        db_manager.rollback()
        print(f"Error inserting fake cars: {error}")


def insert_fake_rentals():
    insert_count = 0

    try:
        while insert_count < 99:

            cars_result = db_manager.fetchall("SELECT id FROM cars;")
            car_ids = [row[0] for row in cars_result]

            users_result = db_manager.fetchall("SELECT id FROM users WHERE status = 'active';")
            user_ids = [row[0] for row in users_result]

            available_cars_result = db_manager.fetchall("SELECT id FROM  cars WHERE status = 'available'")
            available_cars = [row[0] for row in available_cars_result]

            available_users_result = db_manager.fetchall("""
                    SELECT id
                    FROM users
                    WHERE status = 'active'
                    AND id NOT IN (
                        SELECT user_id
                        FROM rentals
                        WHERE status = 'ongoing'
                    );
                """)
            available_users =  [row[0] for row in available_users_result]


            if available_cars and available_users:
                status = random.choice(('returned', 'ongoing'))
            else:
                status = "returned"


            if status == 'returned':
                random_car = random.choice(car_ids)
                random_user = random.choice(user_ids)
                rental_date = fake.date_between(start_date="-1y", end_date="today")
                return_date = fake.date_between(start_date=rental_date, end_date="today")

                args = (random_car, random_user, rental_date, status, return_date)
                query = """
                    INSERT INTO rentals (car_id, user_id, rental_date, status, return_date)
                    VALUES (%s, %s, %s, %s, %s);
                    """

            elif status == "ongoing":
                random_car = random.choice(available_cars)
                random_user = random.choice(available_users)
                rental_date = fake.date_between(start_date="-1y", end_date="today")

                args = (random_user, random_car, rental_date)
                query ="SELECT add_rental(%s, %s, %s)"


            execute_result = db_manager.execute_query(query, *args)
            
            if not execute_result:
                raise Exception("Error executing query")

            insert_count += 1

        db_manager.commit()
        print("Rentals inserted and committed")

    except Exception as error:
        db_manager.rollback()
        print(f"Error inserting fake rentals: {error}")


def main():
    # insert_fake_users()
    # insert_fake_cars()
    insert_fake_rentals()


if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print("Error inserting fake data:", error)