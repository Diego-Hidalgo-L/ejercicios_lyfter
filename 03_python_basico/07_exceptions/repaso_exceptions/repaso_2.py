
def print_index(numbers):
    while True:
        try:
            index = int(input("Ingrese el índice que desea imprimir: "))
            return numbers[index]
        except ValueError:
            print("Ingrese un valor numérico.")
        except IndexError:
            print("No existe el índice en la lista dada.")


def main():
    numbers = [10, 20, 30, 40]
    result = print_index(numbers)
    print(result)


main()