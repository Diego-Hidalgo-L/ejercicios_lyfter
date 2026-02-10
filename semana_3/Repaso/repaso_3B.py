
counter = 1
total_sum = 0
correct_num = 0

while counter <= 3:
    my_num = int(input(f"Ingrese el número {counter}: "))
    
    if my_num == 30:
        correct_num = 30
    
    total_sum += my_num
    counter += 1

if correct_num == 30 or total_sum == 30:
    print("Correcto!")
else:
    print("Incorrecto.")