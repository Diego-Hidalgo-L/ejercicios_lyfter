from orms_4 import User, Address, Car
from faker import Faker
import random

fake = Faker()

def insert_fake_users_with_address():
    user_counter = 0
    address_counter = 0

    try:
        while user_counter < 20:
            # USER:
            username = fake.unique.user_name()
            email = fake.unique.email()
            fullname = fake.name()

            new_user = User(username=username, email=email, fullname=fullname)
            new_user = new_user.add()
            user_counter += 1

            # ADDRESS:
            fake_address = fake.address()

            new_address = Address(user_id=new_user.id, address=fake_address)
            new_address.add()
            address_counter += 1

    except Exception as error:
        print("Error adding fake users and addresses:", error)

    print(f"{user_counter} fake users and {address_counter} addresses inserted and committed to the database")


def insert_fake_cars(): # Podría abrir un session también para consultarle a la base de datos cuántos users hay y asignar user_id's con base en ese dato.
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
    car_counter = 0

    try:
        while car_counter < 20:
            has_owner = random.choice([True, False])

            if has_owner:
                user_id = random.randint(1, 21)
            else:
                user_id = None

            make = random.choice(list(car_models))
            model = random.choice(car_models[make])
            year = random.randint(1990, 2026)

            new_car = Car(user_id=user_id, make=make, model=model, year=year)
            new_car.add()

            car_counter += 1

    except Exception as error:
        print("Error adding fake cars to the database", error)

    print(f"{car_counter} fake cars inserted and committed to the database")


def main():
    insert_fake_users_with_address()
    insert_fake_cars()


if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print("Error inserting fake data:", error)


# diego = User(username="dieqo.hidalqo", email="diego@example.com", fullname="Luis Diego Hidalgo Lara")
# diego.add()

# chevy_tracker = Car(user_id=1, make="Chevrolet", model="Tracker", year=2024)
# chevy_tracker.add()

# my_address = Address(user_id=1, address="San Vicente, Moravia, San José")
# my_address.add()