from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Identity, ForeignKey, Integer, String, Date, CheckConstraint

# Se encarga de crear las tablas y el engine
class DBContext:
    def __init__(self) -> None:
        self.metadata_obj = MetaData(schema="authentication")

        self.users = Table(
            "users",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("username", String(30)),
            Column("password", String),
            Column("role", String(20), CheckConstraint("role in ('Administrator', 'User')"))
        )

        self.products = Table( # No en DB
            "products",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("price", Integer),
            Column("entry_date", Date),
            Column("stock", Integer)
        )

        self.invoices = Table( # No en DB
            "invoices",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
            Column("total_price", Integer, nullable=False)
        )

        self.invoice_products = Table( # No en DB
            "invoice_products",
            self.metadata_obj,
            Column("id", Integer, Identity(), primary_key=True),
            Column("invoice_id", Integer, ForeignKey("invoices.id"), nullable=False),
            Column("product_id", Integer, ForeignKey("products.id"), nullable=False),
            Column("quantity", Integer, nullable=False)
        )

        self.engine = create_engine(
            "postgresql+psycopg2://postgres:xyz0138@localhost:5432/postgres"
        )

        self.metadata_obj.create_all(self.engine)

db_context = DBContext()