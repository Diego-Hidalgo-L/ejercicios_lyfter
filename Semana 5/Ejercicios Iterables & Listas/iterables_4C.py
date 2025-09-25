
# Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_deleted_numbers = []

for index, number in enumerate(my_list):
    if (number % 2 != 0):
        deleted_number = my_list.pop(index)  # Funciona pero no es lo mas correcto porque se mueve el index.
        list_of_deleted_numbers.append(deleted_number)

print(my_list)
print(list_of_deleted_numbers)