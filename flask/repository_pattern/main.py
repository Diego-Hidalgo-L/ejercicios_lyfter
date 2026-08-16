from db import PgManager
from repositories import UsersRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="xyz0138",
    host="localhost"
)

users_repo = UsersRepository(db_manager)

formatted_results = users_repo.get_all()

print(formatted_results)

db_manager.close_connection()