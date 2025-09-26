
# Cree un programa que intercambie el primer y ultimo elemento de una lista.
# Debe funcionar con listas de cualquier tamaño.

my_list = [4, 3, 6, 1, 7]
reversed_list = []

for index in range(len(my_list) -1, -1, -1):
    number = my_list[index]
    reversed_list.append(number)

print(reversed_list)
