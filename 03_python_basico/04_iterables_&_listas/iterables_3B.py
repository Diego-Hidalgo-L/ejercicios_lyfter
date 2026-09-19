
# Cree un programa que intercambie el primer y ultimo elemento de una lista.
# Debe funcionar con listas de cualquier tamaño.

my_list = [4, 3, 6, 1, 7]

new_last_index = my_list.pop(0)
new_first_index = my_list.pop(len(my_list) - 1)
my_list.insert(0, new_first_index)
my_list.append(new_last_index) # mejor practica, porque .append() siempre agrega al final de la lista.
# my_list.insert(len(my_list), new_last_index) SI # NO my_list.insert(len(my_list) - 1, new_last_index): mueve el ultimo indice anterior a la derecha

print(my_list)
