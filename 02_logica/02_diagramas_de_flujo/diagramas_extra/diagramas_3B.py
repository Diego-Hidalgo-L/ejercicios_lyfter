# Cree un diagrama de flujo que pida 3 números al usuario.
    # Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”.
    # Sino, mostrar “Incorrecto”.

list_of_loops = ['primer', 'segundo', 'tercero']
total_sum = 0
correct_number = 0

for loop in list_of_loops:
    new_number = int(input(f"Ingrese el {loop} número: "))
    if (new_number == 30):
        correct_number = 30
    total_sum += new_number

if (correct_number == 30):
    print("Correcto")
elif (total_sum == 30):
        print("Correcto")
else:
    print("Incorrecto")