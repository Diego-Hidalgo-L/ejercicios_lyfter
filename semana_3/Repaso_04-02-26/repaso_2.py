import random 

random_int = random.randint(1, 10)
my_number = 0

while True:
    try:
        my_number = int(input("Please enter a number: "))
    except ValueError:
        print("Error. Please enter a valid integer.")
        continue

    if my_number < 1 or my_number > 10:
        print("Error. Please enter a number between 1 and 10.")
        continue
    
    if my_number == random_int:
        break

    print("Wrong. Try again.")


print("Correct! The random number was:", random_int)