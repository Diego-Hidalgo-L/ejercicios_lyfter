
def convert_input():
    while True:
        try:
            number = int(input("Ingrese un número: "))
            return number
        except ValueError:
            print("Entrada inválida.")


def main():
    number = convert_input()
    print("El número ingresado es:", number)


main()