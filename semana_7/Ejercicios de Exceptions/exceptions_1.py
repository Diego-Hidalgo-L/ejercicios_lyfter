
def show_menu():
    operator = input("""
Ingrese:
- '+' para sumar.
- '-' para restar.
- 'x' para multiplicar.
- '/' para dividir.
- 'C' para borrar.
- 'Stop' para detener el programa
Ingrese el operador que desea: """)
    return operator


def validate_number(prompt):
    while True:
        number = input(prompt)
        try:
            valid_number = float(number)
            return valid_number
        except ValueError:
            print("Ingrese un número válido.")


def sum_number(starting_number):
    new_number = validate_number("Ingrese el número que desea sumar: ")
    result = starting_number + new_number
    return result


def subtract_number(starting_number):
    new_number = validate_number("Ingrese el número que desea restar: ")
    result = starting_number - new_number
    return result


def multiply_number(starting_number):
    new_number = validate_number("Ingrese el número que desea multiplicar: ")
    result = starting_number * new_number
    return result


def divide_number(starting_number):
    while True:
        new_number = validate_number("Ingrese el número por el que desea dividir: ")
        if new_number == 0:
            raise ZeroDivisionError("No se puede dividir entre 0")
        result = starting_number / new_number
        return result


def clear_operation(starting_number):
    starting_number = 0
    return starting_number


def calculate_operation(operator, starting_number):
    if operator == '+':
        sum_result = sum_number(starting_number)
        return sum_result
    elif operator == '-':
        subtraction_result = subtract_number(starting_number)
        return subtraction_result
    elif operator == 'x':
        multiplication_result = multiply_number(starting_number)
        return multiplication_result
    elif operator == '/':
        division_result = divide_number(starting_number)
        return division_result
    elif operator == 'c' or operator == 'C':
        cleared_operation = clear_operation(starting_number)
        return cleared_operation


def main():
    starting_number = 0.0
    print(f"Número inicial: {starting_number}")

    while True:
        try:
            operator = show_menu().strip().lower()

            if operator == "stop":
                break

            if operator not in {'+', '-', 'x', '/', 'c', 'C'}:
                raise ValueError("Operador no reconocido. Use +, -, x, /, C o Stop")

            starting_number = calculate_operation(operator, starting_number)
            print(f"El resultado es: {starting_number}")

        except (ValueError, ZeroDivisionError) as ex:
            print(f"Error: {ex}")

        finally:
            print("Final de la operación.")
    
    print("El programa ha finalizado.")


main()
