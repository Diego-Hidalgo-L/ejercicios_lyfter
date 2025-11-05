# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto.


def ask_for_string():
    my_string = (input("Enter a word: "))
    return my_string


def ask_for_letter():
    my_letter = (input("Enter a letter: "))
    return my_letter


def count_letter(my_string, my_letter):
    letter_counter = 0
    for char in my_string:
        if char == my_letter:
            letter_counter += 1
    return letter_counter


def change_times_var(letter_counter):
    if letter_counter == 1:
        times_var = "time"
    else:
        times_var = "times"
    return times_var


def main():
    my_string = ask_for_string()
    my_letter = ask_for_letter()
    letter_counter = count_letter(my_string, my_letter)
    times_var = change_times_var(letter_counter)
    print(f"The letter '{my_letter}' appears {letter_counter} {times_var}")


main()