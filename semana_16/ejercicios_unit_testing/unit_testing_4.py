
def divide(number1, number2):
    if isinstance(number1, str) or isinstance (number2, str):
        raise TypeError("No se pueden dividir strings.")
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2

