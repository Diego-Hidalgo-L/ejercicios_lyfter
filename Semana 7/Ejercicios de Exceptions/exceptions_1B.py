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


def leer_numero(prompt):
    while True:
        valor = input(prompt)
        try:
            return float(valor)
        except ValueError:
            print("Ingrese un número válido.")


def sum_number(starting_number):
    nuevo = leer_numero("Ingrese el número que desea sumar: ")
    return starting_number + nuevo


def subtract_number(starting_number):
    nuevo = leer_numero("Ingrese el número que desea restar: ")
    return starting_number - nuevo


def multiply_number(starting_number):
    nuevo = leer_numero("Ingrese el número que desea multiplicar: ")
    return starting_number * nuevo


def divide_number(starting_number):
    while True:
        nuevo = leer_numero("Ingrese el número por el que desea dividir: ")
        if nuevo == 0:
            print("No se puede dividir entre cero.")
            continue
        return starting_number / nuevo


def clear_operation(starting_number):
    return 0.0


def calculate_operation(op, starting_number):
    # op ya viene normalizado y validado
    if op == '+':
        return sum_number(starting_number)
    elif op == '-':
        return subtract_number(starting_number)
    elif op == 'x':
        return multiply_number(starting_number)
    elif op == '/':
        return divide_number(starting_number)
    elif op == 'c':
        return clear_operation(starting_number)


def main():
    starting_number = 0.0
    print(f"Número inicial: {starting_number}")

    while True:
        op_raw = show_menu()
        op = op_raw.strip().lower()

        if op == "stop":
            break

        if op not in {'+', '-', 'x', '/', 'c'}:
            print("Operador no reconocido. Use +, -, x, /, C o Stop.")
            continue

        starting_number = calculate_operation(op, starting_number)
        print(f"El resultado es: {starting_number}")

    print("El programa ha finalizado")


main()
