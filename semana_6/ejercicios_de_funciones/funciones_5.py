
# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.


def count_letters_per_case(my_string):
    lower_case = 0
    upper_case = 0
    for char in my_string:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
    return upper_case, lower_case


def main():
    my_string = "I love Nación Sushi"
    upper_case, lower_case = count_letters_per_case(my_string)
    print(f"There are {upper_case} upper cases and {lower_case} lower cases.")


main()