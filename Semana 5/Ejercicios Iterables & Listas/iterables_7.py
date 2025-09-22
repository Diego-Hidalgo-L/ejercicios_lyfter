
# Cree un programa que verifique si todos los elementos de una lista son positivos.

my_list = [3, 6, 0, -2, 4]
negative_number = False

for number in my_list:
    if (number < 1):
        negative_number = True
        break

if (negative_number):
    print("Hay al menos un número negativo o cero")
else:
    print("No hay números negativos")