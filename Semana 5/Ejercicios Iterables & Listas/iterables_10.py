
# Cree un programa que le pida al usuario ingresar 5 palabras.
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras.

my_list = []
target = 5
word_counter = 1

for word in range(target):
    letter_counter = 0
    input_word = input(f"Ingrese la palabra #{word_counter}: ")
    for char in input_word:
        letter_counter += 1

    if letter_counter >= 4:
        my_list.append(input_word)
    
    word_counter += 1

print(my_list)