# Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.

looper = 1
total_sum = 0

while (looper <= 100):
    new_number = int(input(f"Ingrese el número #{looper}: "))
    total_sum += new_number
    looper += 1

print(f"La suma total de los 100 números es de: {total_sum}")