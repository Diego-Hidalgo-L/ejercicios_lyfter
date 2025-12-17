
def add(number1, number2):
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    return number1 + number2


def average(list_of_args):
    total_sum = 0
    for number in list_of_args:
        total_sum += number
    return round(total_sum / len(list_of_args), 2)


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = round(celsius * (9 / 5) + 32, 2)
    return fahrenheit


fahrenheit = convert_celsius_to_fahrenheit(0)
print(fahrenheit)