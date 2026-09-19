
def divide_nums():
    while True:
        try:
            first = float(input("Ingrese el primer número: "))
            second = float(input("ingrese el segundo número: "))
            result = first / second
            return result
        except ValueError:
            print("ValueError: Ingrese valores numéricos.")
        except ZeroDivisionError:
            print("ZeroDivisionError: No se puede dividir entre 0.")


def main():
    result = divide_nums()
    print(result)


main()