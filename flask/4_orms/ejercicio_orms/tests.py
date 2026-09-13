from sqlalchemy.orm import Session
from sqlalchemy import select
from orms_4 import User
from db_engine import engine
import random

value = 20
integer = random.randint(1, value)
print(integer)


string = "83891 Douglas Viaduct Suite 904\nNew Nicole, MI 61110"
print(len(string))


with Session(engine) as session:
    stmt = select(User.id)
    ids = session.scalars(stmt).all()

    print(ids)