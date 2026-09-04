from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import MetaData, ForeignKey, Integer, String
from sqlalchemy import create_engine, select, relationship, back_populates

DB_URI = "postgresql://postgres:xyz0138@localhost:5432/postgres"
engine = create_engine(DB_URI, echo=True)
meta_obj = MetaData(schema="orms")


class Base(DeclarativeBase):
    metadata = meta_obj


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30),unique=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(30), nullable=False)

    addresses: Mapped[list["Address"]] = relationship(back_populates("users")) # 1:N
    cars: Mapped[list["Car"]] = relationship(back_populates("users")) # 1:N

    def get(self):
        try:
            with Session(engine) as session:
                stmt = select(self)
                users = session.scalars(stmt).all

                return users

        except Exception as error:
            print("Error getting users:", error)

    def add(self): # Creo el objeto User AFUERA de la clase
        try:
            with Session(engine) as session:
                result = session.add(self) # Esto retorna algo? Hay una mejor forma de verificar?

                if result:
                    session.commit()
                    print("User added successfully")

        except Exception as error:
            session.rollback()
            print("Error adding user:", error)

    def relate_car(self, car):
        car.self = self

    def modify(self, user_id, mod): # Válido??????
        with Session(engine) as session:
            user = session.get(self, user_id)

            if user:
                mod # Válido??????
                session.commit()
            else:
                print(f"User id {user_id} does not exist")

    def delete(self, user_id):
        with Session(engine) as session:
            user = session.get(self, user_id)

            if user:
                session.delete(user)
                session.commit()
            else:
                print(f"User id {user_id} does not exist")


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False) # "users.id" es el nombre de la columna en SQL - NO objeto Python.
    address: Mapped[str] = mapped_column(String(50), nullable=False)

    user: Mapped["User"] = relationship(back_populates("addresses")) # N:1


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    make: Mapped[str] = mapped_column(String(15), nullable=False)
    model: Mapped[str] = mapped_column(String(15), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=True)

    user: Mapped["User | None"] = relationship(back_populates("cars")) # N:1


Base.metadata.create_all(engine)



# FUERA DE LA TAREA - FINES DIDÁCTICOS:

# with Session(engine) as session:
#     user = User(
#     username = "diegohidalgo",
#     email = "diego@example.com",
#     fullname = "Diego Hidalgo"
# )

#     try:
#         session.add(user)
#         session.commit()
#         print(user.id)

#         users = session.scalars(select(User)).all() # scalars() lo convierte todo en una lista de objetos, EN VEZ de objetos Row
#         print(users)

#     except Exception as error:
#         session.rollback()
#         print("Error adding user:", error)