
def validate_age():
    while True:
        try:
            age = int(input("Ingrese su edad: "))
            if age < 1 or age > 120:
                raise ValueError
            return age
        except ValueError:
            print("Ingrese una edad válida.")


def main():
    age = validate_age()
    print("La edad del usuario es válida:", age)


main()