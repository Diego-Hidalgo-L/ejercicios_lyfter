from faker import Faker
import random
from tarea_3.db import db_manager
from tarea_3.repositories import rentals_repo

fake = Faker()
# print(fake.date())

users_results = db_manager.fetchall("SELECT id FROM users WHERE status = 'active';")
active_users = [row[0] for row in users_results]
ongoing_users = db_manager.fetchall("""
        SELECT rentals.user_id
        FROM rentals
        JOIN users
        ON rentals.user_id = users.id
        WHERE rentals.status = 'ongoing';
    """)
list_ongoing_users = [row[0] for row in ongoing_users]

print(list_ongoing_users)




# Respuesta previa:
def insert_fake_rentals():
    try:
        status_list = ('returned', 'ongoing')
        car_results = db_manager.fetchall("SELECT id FROM cars WHERE status = 'available';")
        car_id_list = [row[0] for row in car_results]
        user_results = db_manager.fetchall("SELECT id FROM users WHERE status = 'active';")
        user_id_list = [row[0] for row in user_results]

        for _ in range(99):
            car_id = random.choice(car_id_list)
            user_id = random.choice(user_id_list)
            rental_date = fake.date_between(start_date="-1y", end_date="today")
            status = random.choice(status_list)

            if status == "returned":
                return_date = fake.date_between(start_date=rental_date, end_date="today")
            else:
                return_date = None

            args = (car_id, user_id, rental_date, status, return_date)
            rentals_query = """
                INSERT INTO rentals (car_id, user_id, rental_date, status, return_date)
                VALUES (%s, %s, %s, %s, %s);
                """

            db_manager.execute_query(rentals_query, *args)

            db_manager.execute_query("UPDATE cars SET status = 'rental ongoing'")

        db_manager.commit()
        print("Rentals inserted and committed")

    except Exception as error:
        db_manager.rollback()
        print("Error inserting fake rentals:", error)



