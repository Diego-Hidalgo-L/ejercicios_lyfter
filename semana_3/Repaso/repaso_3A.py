
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
third_num = int(input("Please enter the third number: "))

if first_num == 30 or second_num == 30 or third_num == 30:
    print("Correct! One of the numbers you entered equals 30.")
elif first_num + second_num + third_num == 30:
    print("Correct! The sum of all the entered numbers is 30.")
else:
    print("None of the conditions apply.")