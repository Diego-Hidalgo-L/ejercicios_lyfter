from datetime import date


date_of_birth = date(2005, 8, 16)
today = date.today()
age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

print(age)