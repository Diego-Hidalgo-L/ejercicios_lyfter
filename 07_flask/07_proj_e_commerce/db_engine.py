from sqlalchemy import create_engine
# import os

DB_URI = "postgresql://postgres:xyz0138@localhost:5432/postgres"
engine = create_engine(DB_URI) # echo=True -> muestra los comandos de SQL en la terminal


# Por si quisiera usar una base de datos de tests:
    # DB_URI = "postgresql://postgres:xyz0138@localhost:5432/{}"
    # DATABASE = "e_commerce_tests" if os.getenv("TESTING") == "1" else "postgres"