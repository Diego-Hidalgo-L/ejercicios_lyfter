from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Identity, ForeignKey, Integer, Float, String, Date, DateTime, CheckConstraint
from datetime import date, timezone

# Se encarga de crear las tablas y el engine

class DBContext:
    def __init__(self) -> None:
        self.metadata_obj = MetaData(schema="authentication")

        self.users = Table(
            "users",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("username", String(30), unique=True, nullable=False),
            Column("password", String, nullable=False),
            Column("role", String(20), CheckConstraint("role in ('Administrator', 'User')"), nullable=False)
        )

        self.contacts = Table(
            "contacts",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
            Column("name", String(30), nullable=False),
            Column("phone", String(8), nullable=False),
            Column("email", String(30), nullable=False)
        )

        self.login_history = Table(
            "login_history",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
            Column("datetime", DateTime(timezone=True), nullable=False),
            Column("ip", String, nullable=False),
            Column("status", String, CheckConstraint("status in ('successful', 'failed')"))
        )

        self.products = Table(
            "products",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("name", String, nullable=False),
            Column("price", Float),
            Column("entry_date", Date),
            Column("stock", Integer)
        )

        self.invoices = Table(
            "invoices",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
            Column("purchase_date", Date, default=date.today) # Estoy pasando la función en sí, no la invocación del método - Si paso 'null' NO genera el default
        )

        self.invoice_products = Table(
            "invoice_products",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("invoice_id", Integer, ForeignKey("invoices.id"), nullable=False),
            Column("product_id", Integer, ForeignKey("products.id"), nullable=False),
            Column("quantity", Integer, nullable=False),
            Column("total_price", Float, nullable=False)
        )

        self.engine = create_engine(
            "postgresql+psycopg2://postgres:xyz0138@localhost:5432/postgres"
        )

        self.metadata_obj.create_all(self.engine)

db_context = DBContext()