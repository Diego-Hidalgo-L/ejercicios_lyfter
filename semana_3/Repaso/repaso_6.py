
counter = 1
total_sum = 0

while counter <= 100:
    my_num = int(input(f"Ingrese el número {counter}: "))
    total_sum += my_num
    counter += 1

print(f"La suma total es de: {total_sum}.")