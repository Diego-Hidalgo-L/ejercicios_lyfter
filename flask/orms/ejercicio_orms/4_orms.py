from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import MetaData, ForeignKey, Integer, String
from sqlalchemy import create_engine, select, relationship, func

DB_URI = "postgresql://postgres:xyz0138@localhost:5432/postgres"
engine = create_engine(DB_URI, echo=True)
meta_obj = MetaData(schema="orms")


class Base(DeclarativeBase):
    metadata = meta_obj


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(30), nullable=False)

    addresses: Mapped[list["Address"]] = relationship(back_populates="user") # 1:N | back_populates = nombre de ese atributo en la otra clase
    cars: Mapped[list["Car"]] = relationship(back_populates="user") # 1:N | back_populates = nombre de ese atributo en la otra clase

    def get_all(self):
        with Session(engine) as session:
            try:
                stmt = select(User)
                users = session.scalars(stmt).all() # scalars() lo convierte todo en una lista de objetos, EN VEZ de objetos Row

                return users

            except Exception as error:
                session.rollback()
                print("Error getting all users:", error)

    def add(self): # Creo el objeto User AFUERA de la clase
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("User added successfully")

            except Exception as error:
                session.rollback()
                print("Error adding user:", error)

    def modify(self, user_id, username=None, email=None, fullname=None):
        with Session(engine) as session:
            try:
                user = session.get(User, user_id)

                if user:
                    if username is not None:
                        user.username = username

                    if email is not None:
                        user.email = email

                    if fullname is not None:
                        user.fullname = fullname
                else:
                    raise Exception(f"User ID {user_id} not found")

                session.commit()
                print(f"User ID {user_id} was modified successfully")

            except Exception as error:
                session.rollback()
                print("Error modifying user:", error)

    def delete(self):
        with Session(engine) as session:
            try:
                user = session.get(User, self.id)

                if user:
                    session.delete(user)
                    session.commit()
                    print("User deleted successfully")
                else:
                    raise ValueError("User not found")

            except Exception as error:
                session.rollback()
                print("Error deleting user:", error)

    def relate_car(self, car_id):
        with Session(engine) as session:
            try:
                car = session.get(Car, car_id)

                if car:
                    self.cars.append(car)
                    session.commit()
                    print("User-car relationship created")
                else:
                    raise ValueError(f"Car ID {car_id} not found")

            except Exception as error:
                session.rollback()
                print("Error creating user-car relationship:", error)

    def unrelate_car(self, car_id):
        with Session(engine) as session:
            try:
                car = session.get(Car, car_id)

                if car in self.cars:
                    self.cars.remove(car)
                    session.commit()
                    print("User-car relationship removed")
                else:
                    raise Exception(f"Relationship with car ID {car.id} not found")

            except Exception as error:
                session.rollback()
                print("Error removing user-car relationship:", error)

    # EXTRA
    def get_users_with_more_than_one_car(self):
        with Session(engine) as session:
            try:
                stmt = select(User).where(len(self.cars) > 1) 
                users = session.scalars(stmt).all()

                # Alternativa:
                stmt2 = (
                    select(Car.user_id, func.count(Car.id))
                    .group_by(Car.user_id)
                    .having(func.count(Car.id) > 1)
                )

                return users

            except Exception as error:
                session.rollback()
                print("Error getting all users with more than one car:", error)

    def print_user_cars(self, user_id):
        with Session(engine) as session:
            try:
                user = session.get(User, user_id)

                if user:
                    print(f"User ID {user_id}'s related cars:")
                    for car in user.cars:
                        print(car)

                else:
                    raise ValueError(f"User ID {user_id} not found")

            except Exception as error:
                session.rollback()
                print("Error printing user's related cars:", error)

    def print_user_addresses(self, user_id):
        with Session(engine) as session:
            try:
                user = session.get(User, user_id)

                if user:
                    print(f"User ID {user_id}'s related addresses:")
                    for address in user.addresses:
                        print(address)

                else:
                    raise ValueError(f"User ID {user_id} not found")

            except Exception as error:
                session.rollback()
                print("Error printing user's related addresses:", error)


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False) # "users.id" es el nombre de la columna en SQL - NO objeto Python.
    address: Mapped[str] = mapped_column(String(50), nullable=False)

    user: Mapped["User"] = relationship(back_populates="addresses") # N:1 | back_populates = nombre de ese atributo en la otra clase

    def get_all(self):
        with Session(engine) as session:
            try:
                stmt = select(Address)
                addresses = session.scalars(stmt).all()

                return addresses

            except Exception as error:
                session.rollback()
                print("Error getting all addresses:", error)

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Address added successfully!")

            except Exception as error:
                session.rollback()
                print("Error adding address:", error)

    def modify(self, address_id, new_address):
        with Session(engine) as session:
            try:
                address = session.get(Address, address_id)

                if address:
                    address.address = new_address
                    session.commit()
                    print(f"Address ID {address_id} was modified successfully")
                else:
                    raise Exception(f"Address ID {address_id} not found")

            except Exception as error:
                session.rollback()
                print("Error modifying address:", error)

    def modify_user_relationship(self, user_id):
        with Session(engine) as session:
            try:
                new_user = session.get(User, user_id)

                if new_user:
                    change = input(f"This address is already related to user ID {self.user_id}. Are you sure you want to change that relationship? [y/n]: ")

                    if change == "y":
                        self.user = new_user
                        session.commit()
                        print(f"Address-user relationship created with user ID {user_id}")
                    else:
                        return

                else:
                    raise ValueError(f"User ID {user_id} not found")

            except Exception as error:
                session.rollback()
                print("Error modifying relationship: ", error)


    def delete(self):
        with Session(engine) as session:
            try:
                address = session.get(Address, self.id)

                if address:
                    session.delete(address)
                    session.commit()
                    print("Address deleted successfully")
                else:
                    raise ValueError("Address not found")

            except Exception as error:
                session.rollback()
                print("Error deleting address:", error)

    # EXTRA
    def get_all_addresses_containing(self, substring):
        with Session(engine) as session:
            try:
                stmt = select(Address).where(Address.address.ilike(f"%{substring}%"))
                addresses = session.scalars(stmt).all()

                return addresses

            except Exception as error:
                session.rollback()
                print(f"Error getting all address that include '{substring}':", error)


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    make: Mapped[str] = mapped_column(String(15), nullable=False)
    model: Mapped[str] = mapped_column(String(15), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=True)

    user: Mapped["User | None"] = relationship(back_populates="cars") # N:1 | back_populates = nombre de ese atributo en la otra clase

    def get_all(self):
        with Session(engine) as session:
            try:
                stmt = select(Car)
                cars = session.scalars(stmt).all()

                return cars

            except Exception as error:
                session.rollback()
                print("Error getting all cars:", error)

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Car added successfully!")

            except Exception as error:
                session.rollback()
                print("Error adding car:", error)

    def modify(self, car_id, make=None, model=None, year=None):
        with Session(engine) as session:
            try:
                car = session.get(Car, car_id)

                if car:
                    if make is not None:
                        car.make = make

                    if model is not None:
                        car.model = model

                    if year is not None:
                        car.year = year
                    
                else:
                    raise Exception(f"Car ID {car_id} not found")

                session.commit()
                print(f"Car ID {car_id} was modified successfully")

            except Exception as error:
                session.rollback()
                print(f"Error modifying car:", error)

    def delete(self):
        with Session(engine) as session:
            try:
                car = session.get(Car, self.id)

                if car:
                    session.delete(car)
                    session.commit()
                    print(f"Car deleted successfully")
                else:
                    raise ValueError("Car not found")

            except Exception as error:
                session.rollback()
                print("Error deleting car:", error)

    def relate_user(self, user_id):
        with Session(engine) as session:
            try:
                new_user = session.get(User, user_id)

                if new_user:
                    if self.user:
                        change = input(f"This car is already related to user ID {self.user_id}. Are you sure you want to change that relationship? [y/n]: ")

                        if change == "y":
                            self.user = new_user
                            session.commit()
                            print(f"Car-user relationship created with user ID {user_id}")
                        else:
                            return
                        
                    else:
                        self.user = new_user
                        session.commit()
                        print(f"Car-user relationship created with user ID {user_id}")

                else:
                    raise ValueError(f"User ID {user_id} not found")

            except Exception as error:
                session.rollback()
                print("Error creating car-user relationship:", error)

    def unrelate_user(self):
        with Session(engine) as session:
            try:
                if self.user:
                    change = input(f"This car is related to user ID {self.user_id}. Are you sure you want to remove that relationship? [y/n]: ")

                    if change == "y":
                        self.user = None
                        session.commit()
                        print("Car-user relationship removed")
                    else:
                        return
                    
                else:
                    print("This car is not related to any user")

            except Exception as error:
                session.rollback()
                print("Error removing car-user relationship:", error)

    # EXTRA
    def get_unrelated_cars(self):
        with Session(engine) as session:
            try:
                stmt = select(Car).where(self.user == None) # self.user.is_(None) | Car.user_id.is_(None)
                unrelated_cars = session.scalars(stmt).all()

                return unrelated_cars

            except Exception as error:
                session.rollback()
                print("Error getting all unrelated cars:", error)



Base.metadata.create_all(engine)

