
from datetime import date

def input_date():
    while True:
        try:
            my_date = input("Please enter a date (YYYY-MM-DD): ")
            if date.fromisoformat(my_date):
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid date in the format YYYY-MM-DD")


formatted_date = input_date()
print(formatted_date)