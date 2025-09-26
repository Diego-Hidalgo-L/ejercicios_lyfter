
# Cree un programa que cuente cuántas veces aparece un número específico en una lista.
# Pida al usuario una lista de números y otro número a buscar.

my_list = [4, 2, 7, 2, 8, 2, 1, 4]
time_strings = ['vez', 'veces']
counter = 0

target = int(input(f"Ingrese el número que desea buscar: "))

for number in my_list:
    if (number == target):
        counter += 1

if (counter == 1):
    print(f"El número {target} aparece {counter} {time_strings[0]}")
else:
    print(f"El número {target} aparece {counter} {time_strings[1]}")
