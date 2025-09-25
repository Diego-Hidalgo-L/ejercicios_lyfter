
# Cree un programa que muestre el valor más pequeño de una lista sin usar min().
    # Use un variable para comparar uno a uno.

my_list = [9, 4, 7, 1, 5]
smallest_number = my_list[0]
correct_index = 0

for i, current_number in enumerate(my_list):
    if (current_number < smallest_number):
        smallest_number = current_number
        correct_index = i


print(f"The smallest number is: {smallest_number}, and it is located in index {correct_index}")
