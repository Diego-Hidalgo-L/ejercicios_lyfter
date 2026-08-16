import psycopg2

def format_user(user_record): # Esta función sirve para cambiar el formato de tuplas en el que vienen los queries por default.
    return {
        "id": user_record[0],
        "full_name": user_record[1],
        "email": user_record[2],
        "password": user_record[3],
    }

connection = psycopg2.connect(
    host="localhost",
    port=5432, # En Postgres siempre es este mismo puerto (Chequear Properties del Server).
    user="postgres",
    password="xyz0138",
    dbname="postgres"
)

print("Connected to the database")

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO python_sql.users (full_name, email, password) values ('Juan Jose Restrepo', 'juan.jo@hotmail.es', '1235');"
)

print("Query executed")

connection.commit()

print("Connection changes committed")



# results = cursor.fetchall()
# formatted_results = [format_user(result) for result in results] # list comprehension
# print(formatted_results)