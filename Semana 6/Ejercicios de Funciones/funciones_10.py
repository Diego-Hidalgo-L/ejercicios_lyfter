# Cree una función que reciba un string y retorne cuántas vocales contiene.


def ask_for_string():
    my_string = input("Please enter a phrase: ")
    my_string = my_string.lower()
    return my_string


def count_vowels(my_string):
    vowel_counter = 0
    for char in my_string:
        if char in "aeiou":
            vowel_counter += 1
    return vowel_counter


def main():
    my_string = ask_for_string()
    vowel_counter = count_vowels(my_string)
    print(f"The phrase contains {vowel_counter} vowels")


main()