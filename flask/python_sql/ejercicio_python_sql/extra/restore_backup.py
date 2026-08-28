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

def insert_users_(users_data):
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

        print("All users were inserted successfully!")
        wanna_commit = input("Want to commit to the database? [y/n]")

        if wanna_commit == "y":
            db_manager.commit()

    except Exception as error:
        db_manager.rollback()
        print(f"Error backing up users: {error}")




users = read_csv_backups("extra/db_backups/users_backup_2026-08-26.csv")
insert_users_(users)