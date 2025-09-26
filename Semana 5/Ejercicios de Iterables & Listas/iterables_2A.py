
# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = 'Pizza con piña'

for index in range(len(my_string) -1, -1, -1): # el segundo espacio es para indicarle DONDE PARAR (para al llegar a ese index, no printea).
    char = my_string[index]                    # el tercer espacio (-1) indica la dirección en la que corre el loop.
    print(char)