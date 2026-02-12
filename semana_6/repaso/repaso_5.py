
def count_chars(my_str):
    upper = lower = digits = 0

    for char in my_str:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            digits += 1

    return upper, lower, digits


def main():
    my_str = "Hola123Mundo"
    upper, lower, digits = count_chars(my_str)
    print("Upper:", upper)
    print("Lower:", lower)
    print("Digits:", digits)


main()