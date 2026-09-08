from sqlalchemy.orm import Session
from sqlalchemy import select
from orms_4 import User, Address, Car
from db_engine import engine
from faker import Faker
import random

fake = Faker()

def add_fake_users_with_address():
    counter = 0
    
    with Session(engine) as session:
        try:
            while counter < 20:
                username = fake.unique.user_name()
                email = fake.unique.email()
                fullname = fake.name()
                new_user = User(username=username, email=email, fullname=fullname)

                session.add(new_user) 
                session.flush()

                fake_address = fake.address()
                new_address = Address(user_id=new_user.id, address=fake_address)

                session.add(new_address)
                session.flush()

                counter += 1

            session.commit()
            print(f"{counter} fake users and addresses added and committed to the database successfully")

        except Exception as error:
            session.rollback()
            raise Exception("Error adding fake users and addresses:", error)


def add_fake_cars():
    car_models = {
        "Toyota": [
            "Corolla",
            "Camry",
            "RAV4",
            "Prius",
            "Hilux",
            "Land Cruiser"
        ],
        "Honda": [
            "Civic",
            "Accord",
            "CR-V",
            "HR-V",
            "Pilot",
            "Odyssey"
        ],
        "Ford": [
            "Mustang",
            "F-150",
            "Explorer",
            "Escape",
            "Bronco",
            "Ranger"
        ],
        "Chevrolet": [
            "Malibu",
            "Camaro",
            "Corvette",
            "Tahoe",
            "Suburban",
            "Equinox"
        ],
        "Nissan": [
            "Sentra",
            "Altima",
            "Rogue",
            "Pathfinder",
            "Frontier",
            "Versa"
        ],
        "Hyundai": [
            "Elantra",
            "Sonata",
            "Tucson",
            "Santa Fe",
            "Kona",
            "Palisade"
        ],
        "Kia": [
            "Forte",
            "K5",
            "Sportage",
            "Sorento",
            "Telluride",
            "Seltos"
        ],
        "Volkswagen": [
            "Golf",
            "Jetta",
            "Passat",
            "Tiguan",
            "Taos",
            "Atlas"
        ],
        "BMW": [
            "3 Series",
            "5 Series",
            "7 Series",
            "X3",
            "X5",
            "X7"
        ],
        "Mercedes-Benz": [
            "A-Class",
            "C-Class",
            "E-Class",
            "S-Class",
            "GLC",
            "GLE"
        ],
        "Mazda": [
            "Mazda3",
            "Mazda6",
            "CX-3",
            "CX-5",
            "CX-30",
            "CX-90"
        ],
        "Subaru": [
            "Impreza",
            "Legacy",
            "Outback",
            "Forester",
            "Crosstrek",
            "Ascent"
        ]
    }
    counter = 0

    with Session(engine) as session:
        try:
            ids = session.scalars(select(User.id)).all()

            while counter < 20:
                has_owner = random.choice([True, False])

                if has_owner:
                    user_id = random.choice(ids)
                else:
                    user_id = None

                make = random.choice(list(car_models))
                model = random.choice(car_models[make])
                year = random.randint(1990, 2026)

                new_car = Car(user_id=user_id, make=make, model=model, year=year)
                session.add(new_car)
                session.flush()

                counter += 1

            session.commit()
            print(f"{counter} fake cars inserted and committed to the database successfully")

        except Exception as error:
            session.rollback()
            raise Exception(f"Error adding car number {counter}:", error)


def main():
    add_fake_users_with_address()
    add_fake_cars()


if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print(error)


# diego = User(username="dieqo.hidalqo", email="diego@example.com", fullname="Luis Diego Hidalgo Lara")
# diego.add()

# chevy_tracker = Car(user_id=1, make="Chevrolet", model="Tracker", year=2024)
# chevy_tracker.add()

# my_address = Address(user_id=1, address="San Vicente, Moravia, San José")
# my_address.add()