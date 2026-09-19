
# Cree un programa que le pida al usuario 10 números.
# Al final muestre todos los números que ingresó, seguido del numero ingresado más alto.

list_of_numbers = []
bigger_number = 0
counter = 1

target = 10

for number in range(target):
    new_number = int(input(f"Ingrese el número #{counter}: "))
    list_of_numbers.append(new_number)
    if (new_number > bigger_number):
        bigger_number = new_number
    counter += 1

print(f"La lista de números es: {list_of_numbers}")
print(f"El número más alto es: {bigger_number}")