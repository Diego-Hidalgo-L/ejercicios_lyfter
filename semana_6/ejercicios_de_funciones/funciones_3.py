# Cree una función que retorne la suma de todos los números de una lista.
    # La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).


def sum_of_numbers(numbers_list):
    total_sum = 0
    for number in numbers_list:
        total_sum += number
    return total_sum


def main():
    numbers_list = [4, 6, 2, 29]
    total_sum = sum_of_numbers(numbers_list)
    print(total_sum)


main()