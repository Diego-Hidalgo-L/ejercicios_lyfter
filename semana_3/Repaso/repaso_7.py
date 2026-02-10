
counter = 1
big_num = 0

while counter <= 100:
    my_num = int(input(f"Ingrese el número {counter}:"))
    if my_num > big_num:
        big_num = my_num
    counter += 1

print(f"El número mayor es: {big_num}.")