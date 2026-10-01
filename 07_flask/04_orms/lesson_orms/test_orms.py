import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy import insert

print(sqlalchemy.__version__) # 2.0.52

DB_URI = 'postgresql://postgres:xyz0138@localhost:5432/postgres' # postgresql://<username>:<password>@<host>:<port>/<database>
engine = create_engine(DB_URI, echo=True)

try:
    connection = engine.connect()
    print("Connection successful!")

    metadata_obj = MetaData(schema="public") # "public" es el default si no especifico ningún schema

    user_table = Table(
        "users",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String)
    )

    address_table = Table(
        "addresses",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
        Column("email_address", String, nullable=False)
    )

    metadata_obj.create_all(engine)

    # insert_stmt = insert(user_table).values(name = "spongebob", fullname = "SpongeBob Squarepants")


    insert_stmt =  insert(user_table).values(
        [
            {"name": "calamardo", "fullname": "Calamardo"},
            {"name": "don cangrejo", "fullname": "Don Cangrejo Bolsón"}
        ]
        ).returning(user_table.c.id, user_table.c.name)

    result = connection.execute(insert_stmt)

    print(result)
    
    connection.commit()

    connection.close()

except Exception as error:
    connection.rollback()
    print("Connection failed:", error)