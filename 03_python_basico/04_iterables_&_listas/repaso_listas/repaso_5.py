
my_list = []
big_num = None # Mejor - por si se ingresan solo números negativos.

while True:
    number = input("Ingrese un número: ")
    if number == 'stop':
        break
    
    try:
        number = int(number)
    except ValueError:
        print("Ingrese un número válido o 'stop'.")
        continue

    if big_num is None or number > big_num:
        big_num = number
    
    my_list.append(number)


print("Números ingresados:", my_list)
print("El número más alto fue:", big_num)