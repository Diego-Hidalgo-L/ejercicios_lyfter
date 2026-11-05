from db import Base, User, Product, Invoice, InvoiceProduct, BillingAddress, PaymentMethod, UserPaymentMethod
from db_engine import engine

if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine)
        print("Tables created successfully")

    except Exception as error:
        print(f"Error creating tables:", error)