from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Identity, Integer, String, CheckConstraint

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

        self.engine = create_engine(
            "postgresql+psycopg2://postgres:xyz0138@localhost:5432/postgres"
        )

        self.metadata_obj.create_all(self.engine)

db_context = DBContext()