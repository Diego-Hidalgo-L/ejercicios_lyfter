
my_list = []
big_num = 0

while True:
    number = input("Ingrese un número: ")
    if number == 'stop':
        break
    else:
        number = int(number)
        if number > big_num:
            big_num = number
        my_list.append(number)


print("Números ingresados:", my_list)
print("El número más alto fue:", big_num)