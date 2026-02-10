
numbers = [1, 2, 3, 4, 5, 6]
pares = []
impares = []

for number in numbers:
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)


print("Pares:", pares)
print("Impares:", impares)