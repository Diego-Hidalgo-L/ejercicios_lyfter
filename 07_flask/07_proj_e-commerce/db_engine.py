from db import Base, User, Product, Invoice, InvoiceProduct
from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:xyz0138@localhost:5432/postgres"
engine = create_engine(DB_URI) # echo=True -> muestra los comandos de SQL en la terminal

if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine)
        print("Tables created successfully")

    except Exception as error:
        print(f"Error creating tables:", error)