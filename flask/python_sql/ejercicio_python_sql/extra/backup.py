import csv
from datetime import date
from pathlib import Path
from tarea_3.db import db_manager
from tarea_3.functions import format_users, format_cars, format_rentals

def backup_tables(path, data, headers):
    with open(path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    today = date.today()

    backups_folder = Path("extra/db_backups")
    if not backups_folder.exists():
        backups_folder.mkdir()
        print("'db_backups' folder was created")

    users_path = backups_folder/f"users_backup_{today}.csv"
    cars_path = backups_folder/f"cars_backup_{today}.csv"
    rentals_path = backups_folder/f"rentals_backup_{today}.csv"

    users_results, users_headers = db_manager.fetchall_with_headers("SELECT * FROM users ORDER BY id ASC;")
    users_data = [format_users(user) for user in users_results]
    backup_tables(users_path, users_data, users_headers)

    cars_results, cars_headers = db_manager.fetchall_with_headers("SELECT * FROM cars ORDER BY id ASC;")
    cars_data = [format_cars(car) for car in cars_results]
    backup_tables(cars_path, cars_data, cars_headers)

    rentals_results, rentals_headers = db_manager.fetchall_with_headers("SELECT * FROM rentals ORDER BY id ASC;")
    rentals_data = [format_rentals(rental) for rental in rentals_results]
    backup_tables(rentals_path, rentals_data, rentals_headers)

    print("Tables backed-up successfully")


if __name__ == "__main__":
    try:
        main()
        
    except Exception as error:
        print("Backup failed:", error)