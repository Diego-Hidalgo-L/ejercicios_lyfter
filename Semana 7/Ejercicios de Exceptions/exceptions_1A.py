

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


def calculate_operation(operator, starting_number):
    if operator in "+ - x / C stop Stop":
        if operator == '+':
            sum_result = sum_number(operator, starting_number)
            return sum_result
        elif operator == '-':
            subtraction_result = subtract_number(operator, starting_number)
            return subtraction_result
        elif operator == 'x':
            multiplication_result = multiply_number(operator, starting_number)
            return multiplication_result
        elif operator == '/':
            division_result = divide_number(operator, starting_number)
            return division_result
        elif operator == 'C':
            operation_cleared = clear_operation(operator, starting_number)
            return operation_cleared
        
        elif operator == "Stop" or operator == "stop":
            stop = 'stop'
            return stop
        
    raise ValueError("Ingrese un operador válido.")


def sum_number(operator, starting_number):
    if operator == '+':
        try:
            new_number = int(input("Ingrese el número que desea sumar: "))
            new_number += starting_number
            return new_number
        except ValueError as ex:
            raise ValueError(f"{ex}. Ingrese un número válido")


def subtract_number(operator, starting_number):
    if operator == '-':
        try:
            new_number = int(input("Ingrese el número que desea restar: "))
            starting_number -= new_number
            return starting_number
        except ValueError as ex:
            raise ValueError(f"{ex}. Ingrese un número válido")


def multiply_number(operator, starting_number):
    if operator == 'x':
        try:
            new_number = int(input("Ingrese el número que desea multiplicar: "))
            starting_number *= new_number
            return starting_number
        except ValueError as ex:
            raise ValueError(f"{ex}. Ingrese un número válido")


def divide_number(operator, starting_number):
    if operator == '/':
        try:
            new_number = int(input("Ingrese el número que desea dividir: "))
            if new_number == 0:
                raise ZeroDivisionError("No se puede dividir entre 0")
            else:
                starting_number /= new_number
            return starting_number
        except ValueError as ex:
            raise ValueError(f"{ex}. Ingrese un número válido")


def clear_operation(operator, starting_number):
        return 0.0


def main():
    starting_number = 0
    print(f"Número inicial: {starting_number}")
    
    while starting_number != "stop":
        try:
            operator = show_menu()
            starting_number = calculate_operation(operator, starting_number)
            print(f"El resultado es: {starting_number}")
        except Exception as ex:
            print(f"{ex}. Ingrese un número válido.")
    print("El programa ha finalizado")


main()