
# Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_list = []

for number in my_list:
    if (number % 2 == 0):  # Funciona pero no es lo mas correcto porque se mueve el index.
        evens_list.append(number)

print(evens_list)