

# 4. Cree un programa que le pida tres números al usuario y muestre el mayor.

list_of_loops = ['first', 'second', 'third']
bigger_number = 0

for loop in list_of_loops:
    number = int(input(f"Please enter the {loop} number: "))
    if (number > bigger_number):
        bigger_number = number

print(f"The bigger number is: {bigger_number}")