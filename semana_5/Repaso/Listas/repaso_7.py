
numbers = [1, 3, 5, 6, 7]
is_sorted = "SÍ"

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = "NO"
        break


print(f"La lista {is_sorted} está ordenada.")