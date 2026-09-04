
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

print(sqlalchemy.__version__)

DB_URI = "postgresql://postgres:xyz0138@localhost:5432/postgres"
engine = create_engine(DB_URI, echo=True)


try:
    with engine.connect() as conn:
        print("Connection successful!")

        meta_obj = MetaData(schema="orms")

        user_table = Table(
            "users",
            meta_obj,
            Column("id", Integer, primary_key=True),
            Column("username", String(30), unique=True, nullable=False),
            Column("email", String(30), unique=True, nullable=False),
            Column("fullname", String(30), nullable=False)
        )

        address_table = Table(
            "addresses",
            meta_obj,
            Column("id", Integer, primary_key=True),
            Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
            Column("address", String(50), nullable=False)
        )

        car_table = Table(
            "cars",
            meta_obj,
            Column("id", Integer, primary_key=True),
            Column("user_id", Integer, ForeignKey("users.id"), nullable=True),
            Column("make", String(15), nullable=False),
            Column("model", String(15), nullable=False),
            Column("year", Integer, nullable=True)
        )

        meta_obj.create_all(engine)

except Exception as error:
    print("Connection failed:", error)