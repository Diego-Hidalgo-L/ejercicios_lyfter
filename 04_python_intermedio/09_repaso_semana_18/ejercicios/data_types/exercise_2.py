
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

while True:
    try:
        age = int(input("Enter your age: "))

        if 0 < age < 100:
            break

        print("Invalid age. Please enter a number between 1 and 99")

    except ValueError:
        print("Please enter a whole number")


LEGAL_ADULT_AGE = 18
PRESIDENT_AGE = 35

legal = age >= LEGAL_ADULT_AGE
president = age >= PRESIDENT_AGE


if age <= 2:
    category = "Baby"

elif 3 <= age <= 5:
    category = "Toddler"

elif 6 <= age <= 10:
    category = "Child"

elif 11 <= age <= 12:
    category = "Pre-teen"

elif 13 <= age <= 17:
    category = "Teenager"

elif 18 <= age <= 25:
    category = "Young Adult"

elif 26 <= age <= 59:
    category = "Adult"

else:
    category = "Senior"


print(f"\nHello, {first_name} {last_name}!")
print("Category:", category)
print("Legal adult:", "Yes" if legal else "No")
print("Can run for US President:", "Yes" if president else "No")