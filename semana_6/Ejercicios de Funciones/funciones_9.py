# Cree una función que reciba una lista de palabras y un número n.
# Retorne una nueva lista con solo las palabras que tengan más de n letras.


def ask_for_words():
    my_list = []
    word_target = 5
    word_counter = 1
    while word_counter <= word_target: # técnicamente más correcto un "for" loop:   for word_counter in range(1, word_target + 1):
        new_word = (input(f"Ingrese la palabra #{word_counter} de {word_target}: "))
        my_list.append(new_word)
        word_counter += 1
    return my_list


def ask_for_letter_minimum():
    letter_minimum = int(input("Ingrese el número mínimo de letras: "))
    return letter_minimum


def count_letters(my_list, letter_minimum):
    new_list = []
    for word in my_list:
        letter_counter = 0
        for char in word:
            letter_counter += 1
        if letter_counter > letter_minimum:
            new_list.append(word)
    return new_list


def main():
    my_list = ask_for_words()
    letter_minimum = ask_for_letter_minimum()
    new_list = count_letters(my_list, letter_minimum)
    print(f"La lista de palabras que superan el mínimo de letras es: {new_list}")


main()