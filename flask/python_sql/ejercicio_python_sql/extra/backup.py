import csv
from datetime import date
from tarea_3.repositories import users_repo, cars_repo, rentals_repo

def backup_tables(path, data, headers):
    with open(path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    filters = None
    today = date.today()

    users_data = users_repo.get_users(filters)
    backup_tables(f"flask/python_sql/ejercicios_python_sql/extra/db_backups/users_backup_{today}.csv", users_data, users_data[0].keys())

    cars_data = cars_repo.get_cars(filters)
    backup_tables(f"flask/python_sql/ejercicios_python_sql/extra/db_backups/cars_backup_{today}.csv", cars_data, cars_data[0].keys())

    rentals_data = rentals_repo.get_rentals(filters)
    backup_tables(f"flask/python_sql/ejercicios_python_sql/extra/db_backups/rentals_backup_{today}.csv", rentals_data, rentals_data[0].keys())

    print("Tables backed-up successfully")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Backup failed:", error)