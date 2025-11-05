# Cree un diagrama de flujo que pida 3 números al usuario.
    # Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”.
    # Sino, mostrar “Incorrecto”.

first_number = int(input("Ingrese el primer número: "))
second_number = int(input("Ingrese el segundo número: "))
third_number = int(input("Ingrese el tercer número: "))

if (first_number == 30 or second_number == 30 or third_number == 30):
    print("Correcto")
elif (first_number + second_number + third_number == 30):
    print("Correcto")
else:
    print("Incorrecto")