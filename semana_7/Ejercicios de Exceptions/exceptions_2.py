

def ask_for_name():
    name = input(f"Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número.")
    return name


def ask_for_age():
    age_str = input("Ingrese su edad: ")
    try:
        age = int(age_str)
        if age < 1 or age > 100:
            raise ValueError("La edad no es válida.")
        return age
    except ValueError:
        raise ValueError("La edad no es válida.")
    

def print_happy_path(name, age):
    print(f"¡Hola, {name}! Su edad es de {age} años.")


def main():
    try:
        name = ask_for_name()
        age = ask_for_age()
        print_happy_path(name, age)
    except Exception as ex:
        print(f"Error: {ex}")


main()