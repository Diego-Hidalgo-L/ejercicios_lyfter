# 4.	Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.

looper = 1
bigger_number = 0

while (looper <= 5):
    new_number = int(input(f"Ingrese el número #{looper}: "))
    if (new_number > bigger_number):
        bigger_number = new_number
    looper += 1

print(f"El número mayor es: {bigger_number}")