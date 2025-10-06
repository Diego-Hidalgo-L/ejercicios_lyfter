
import re

def input_student_section():
    pattern = r"^(1[0-2]|[1-9])[A-Ca-c]$"
    while True:
        student_section = input("Please enter the student's section: ").upper()

        if re.match(pattern, student_section):
            print(student_section)
            break
        else:
            print("\nInvalid section format. Please try again. ")


input_student_section()