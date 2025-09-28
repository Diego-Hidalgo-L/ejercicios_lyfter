
# Cree un programa que reciba una lista de números y calcule el promedio de los valores.
# Luego cree una nueva lista con solo los valores mayores al promedio.

my_list = [10, 20, 30, 40, 50]
total_sum = 0
average = 0
new_list = []

for number in my_list:
    total_sum += number

average = total_sum / len(my_list)

for number in my_list:
    if (number > average):
        new_list.append(number)

print(f"El promedio es: {average}")
print(f"Los números arriba del promedio son: {new_list}")