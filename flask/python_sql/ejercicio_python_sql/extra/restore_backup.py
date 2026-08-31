import csv
from tarea_3.db import db_manager

def read_csv_backups(path):
    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        
        for row in reader:
            row_dict = {}
            for key, value in row.items():
                row_dict[key] = value
            data.append(row_dict)

        return data


def insert_users(users_data):
    try:
        query = """
            INSERT INTO users (full_name, email, username, password, date_of_birth, status)
            VALUES (%s, %s, %s, %s, %s, %s);
            """

        user_count = 0

        for user in users_data:
            full_name = user.get("full_name")
            email = user.get("email")
            username = user.get("username")
            password = user.get("password")
            date_of_birth = user.get("date_of_birth")
            status = user.get("status")
    
            args = (full_name, email, username, password, date_of_birth, status)

            execute_result = db_manager.execute_query(query, *args)

            if not execute_result:
                raise Exception("Error inserting users")

            user_count += 1

        print(f"All {user_count} users were inserted successfully!")
        wanna_commit = input("Want to commit to the database? [y/n]: ")

        if wanna_commit.strip().lower() == "y":
            db_manager.commit()
            print("Commitment successful")
        else:
            db_manager.rollback()
            print("Rolled back")

    except Exception as error:
        db_manager.rollback()
        print(f"Error backing up users: {error}")


def insert_cars(cars_data):
    try:
        query = """
            INSERT INTO cars (license_plate, brand, model, year, status)
            VALUES (%s, %s, %s, %s, %s);
            """

        car_count = 0

        for car in cars_data:
            license_plate = car.get("license_plate")
            brand = car.get("brand")
            model = car.get("model")
            year = car.get("year")
            status = car.get("status")
    
            args = (license_plate, brand, model, year, status)

            execute_result = db_manager.execute_query(query, *args)

            if not execute_result:
                raise Exception("Error inserting cars")

            car_count += 1

        print(f"All {car_count} cars were inserted successfully!")
        wanna_commit = input("Want to commit to the database? [y/n]: ")

        if wanna_commit.strip().lower() == "y":
            db_manager.commit()
            print("Commitment successful")
        else:
            db_manager.rollback()
            print("Rolled back")

    except Exception as error:
        db_manager.rollback()
        print(f"Error backing up cars: {error}")


def insert_rentals(rentals_data):
    try:
        query = """
            INSERT INTO rentals (car_id, user_id, rental_date, status, return_date)
            VALUES (%s, %s, %s, %s, %s);
            """

        rental_count = 0

        for rental in rentals_data:
            car_id = rental.get("car_id")
            user_id = rental.get("user_id")
            rental_date = rental.get("rental_date")
            status = rental.get("status")
            return_date = rental.get("return_date")

            if return_date == '':
                return_date = None
    
            args = (car_id, user_id, rental_date, status, return_date)

            execute_result = db_manager.execute_query(query, *args)

            if not execute_result:
                raise Exception("Error inserting rentals")

            rental_count += 1

        print(f"All {rental_count} rentals were inserted successfully!")
        wanna_commit = input("Want to commit to the database? [y/n]: ")

        if wanna_commit.strip().lower() == "y":
            db_manager.commit()
            print("Commitment successful")
        else:
            db_manager.rollback()
            print("Rolled back")

    except Exception as error:
        db_manager.rollback()
        print(f"Error backing up rentals: {error}")

def main():
    restore_users = input("Want to restore users table? [y/n]: ")

    if restore_users.strip().lower() == "y":
        users_data = read_csv_backups("extra/db_backups/users_backup_2026-08-26.csv")
        insert_users(users_data)


    restore_cars = input("Want to restore cars table? [y/n]: ")

    if restore_cars.strip().lower() == "y":
        cars_data = read_csv_backups("extra/db_backups/cars_backup_2026-08-26.csv")
        insert_cars(cars_data)


    restore_rentals = input("Want to restore cars table? [y/n]: ")

    if restore_rentals.strip().lower() == "y":
        rentals_data = read_csv_backups("extra/db_backups/rentals_backup_2026-08-22.csv")
        insert_rentals(rentals_data)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error backing up: {error}")