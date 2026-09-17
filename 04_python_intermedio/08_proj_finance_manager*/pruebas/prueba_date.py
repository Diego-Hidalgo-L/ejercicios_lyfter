
from datetime import date

def input_date():
    while True:
        try:
            my_date = input("Please enter a date (YYYY-MM-DD): ")
            parsed_date = date.fromisoformat(my_date)
            today = date.today()

            if parsed_date > today:
                return "Error"
            else:
                return "OK"
        except ValueError:
            print("Please enter a valid date in the format YYYY-MM-DD")


formatted_date = input_date()
print(formatted_date)
