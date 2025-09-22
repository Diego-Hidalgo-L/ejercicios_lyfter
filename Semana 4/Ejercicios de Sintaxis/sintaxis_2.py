

# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad.
    # Muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Please enter your name: ")
last_name = input("Please enter your last name: ")
age = int(input("Please enter your age: "))

if (age < 2):
    print(f"{name} {last_name} is a baby or infant.")
elif (3 <= age <= 9):
    print(f"{name} {last_name} is a child.")
elif (10 <= age <= 12):
    print(f"{name} {last_name} is a pre-teen or preadolescent.")
elif (13 <= age <= 19):
    print(f"{name} {last_name} is a teenager or adolescent.")
elif (20 <= age <= 35):
    print(f"{name} {last_name} is a young adult.")
elif (36 <= age <= 64):
    print(f"{name} {last_name} is an adult.")
else:
    print(f"{name} {last_name} is a senior.")