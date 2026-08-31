from db import PgManager

db_manager = PgManager(
    db_name='postgres',
    user='postgres',
    password='xyz0138',
    host='localhost'
    )

def format_users(user_record):
    return {
        "id": user_record[0],
        "full_name": user_record[1],
        "email": user_record[2],
        "password": user_record[3]
    }

results = db_manager.execute_query("SELECT * FROM python_sql.users;")
formatted_results = [format_users(result) for result in results]

print(formatted_results)

db_manager.close_connection()