
# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = 'Pizza con piña'

for index in range(len(my_string) -1, -1, -1):
    char = my_string[index]                    
    print(char)


# len(my_string) -1 es desde donde tiene que empezar (el último índice)
# el segundo -1 es para indicarle DONDE PARAR (PARA al llegar a ese index, NO printea).
# el tercer -1 indica la dirección en la que corre el loop.