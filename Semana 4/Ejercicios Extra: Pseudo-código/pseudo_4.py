# Cree un algoritmo que le pida 2 números al usuario.
    # Guárdelos en dos variables distintas (primero y segundo).
    # Ordénelos de menor a mayor en dichas variables. 

first_number = int(input("Ingrese el primer número: "))
second_number = int(input("Ingrese el segundo número: "))

if (first_number < second_number):
    print(first_number)
    print(second_number)
else:
    print(second_number)
    print(first_number)