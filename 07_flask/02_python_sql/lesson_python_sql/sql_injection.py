import psycopg2


# Endpoint hipotético

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="xyz0138",
    dbname="postgres",
)
print("Connected to database!")

request_body = {
    "full_name": "Juan Jose Restrepo', 'juan.jo@hotmail.es', '1235'); DELETE FROM lyfter_duad.users; --",
    "email": "joseaa154@gmail.com",
    "password": "ASFDSA@!",
}

full_name = request_body.get("full_name")
email = request_body.get("email")
password = request_body.get("password")

cursor = connection.cursor()

cursor.execute(
    f"INSERT INTO python_sql.users (full_name, email, password) values (%s, %s, %s);",
    (full_name, email, password)
)
print("Query executed")

connection.commit()
print("Connection changes committed")