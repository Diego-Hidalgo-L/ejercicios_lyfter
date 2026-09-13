from tarea_3.db import db_manager

def verify_tables():
    query = """
        SELECT COUNT(table_name)
        FROM information_schema.tables
        WHERE table_schema = 'lyfter_car_rental'
            AND table_name IN ('users', 'cars', 'rentals');
        """

    result = db_manager.fetchall(query)
    table_count = result[0][0]

    return table_count == 3


def verify_cars_table():
    query = """
        SELECT id
        FROM cars
        WHERE status = 'available';
        """

    result = db_manager.fetchall(query)

    if not result:
        return "DB ERROR: No cars available"
    else:
        return "DB OK: System operating normally"


def main():
    if db_manager.connection:
        print("Database is connected")
        tables_verification = verify_tables()

        if not tables_verification:
            print("DB ERROR: The tables don't exist ('users', 'cars', 'rentals')")
        else:
            print("All tables exist: 'users', 'cars, 'rentals'")
            cars_verification = verify_cars_table()
            print(cars_verification)
    else:
        raise Exception("Database connection unavailable")


if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print("Health verification failed:", error)

