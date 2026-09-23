
def divide():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if b == 0:
                raise ZeroDivisionError
            return a / b
        except TypeError:
            print("Ingrese valores válidos.")
        except ValueError:
            print("Ingrese valores válidos.")
        except ZeroDivisionError:
            print("No se puede dividir entre 0.")


def main():
    result = divide()
    print("El resultado de la división es:", result)


main()