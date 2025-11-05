
multiplier = 1
list_of_results = []

my_number = int(input("Ingrese un número 1 al 10: "))

if (1 <= my_number <= 10):
    while (multiplier <= 12):
        result = my_number * multiplier
        list_of_results.append(f"{my_number} x {multiplier} = {result}")
        multiplier += 1
    print(f"La tabla del {my_number} es:")
    
    for item in list_of_results:
        print(item)
else:
    print("El número no es válido.")
