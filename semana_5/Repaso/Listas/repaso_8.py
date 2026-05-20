
numbers = [1, 2, 3, 4, 5, 6]
pares = []
impares = []

for number in numbers:
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)

    # Opción 2: La MEJOR
# pares = [n for n in numbers if n % 2 == 0]
# impares = [n for n in numbers if n % 2 != 0]


print("Pares:", pares)
print("Impares:", impares)