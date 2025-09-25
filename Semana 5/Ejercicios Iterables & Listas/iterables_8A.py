
# Cree un programa que muestre el valor más pequeño de una lista sin usar min().
    # Use un variable para comparar uno a uno.

my_list = [9, 4, 7, 1, 5]
smallest_number = my_list[0]

for current_number in my_list:
    if (current_number <= smallest_number):
        smallest_number = current_number


print(f"El menor valor es: {smallest_number}")