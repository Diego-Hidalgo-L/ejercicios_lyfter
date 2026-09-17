# Cree un algoritmo que le pida un numero al usuario.
# Realice una suma de cada numero del 1 hasta ese número ingresado.
# Luego muestre el resultado de la suma.

counter = 1
total_sum = 0

number = int(input("Please enter a number: "))
while (counter <= number):
    total_sum += counter
    counter += 1

print(f'The total sum equals: {total_sum}')