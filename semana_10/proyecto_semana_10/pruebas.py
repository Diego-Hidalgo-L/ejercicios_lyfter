
from students_info import students_list

def input_student_info():
    student_name = input("Please enter the student's full name: ")
    student_section = input("Please enter the student's section: ")
    
    return student_name, student_section


def validate_grade_number(prompt):
    while True:
        number = input(prompt)
        try:
            valid_number = float(number)
            if 1 <= valid_number <= 100:
                return valid_number
            else:
                print("\nInvalid answer. Please enter a grade from 1 to 100.")
        except ValueError:
            print("\nInvalid answer. Please enter a valid number.")


def input_grades():
    spanish_grade = validate_grade_number("Please enter the student's Spanish grade: ")
    english_grade = validate_grade_number("Please enter the student's English grade: ")
    social_grade = validate_grade_number("Please enter the student's Social Studies grade: ")
    science_grade = validate_grade_number("Please enter the student's Science grade: ")

    return spanish_grade, english_grade, social_grade, science_grade


def calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade): # optimize to not be limited to just 4 subjects
    individual_avg = (spanish_grade + english_grade + social_grade + science_grade) / 4

    return individual_avg


def create_dict_entry(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg):
    dict_entry = {}
    
    dict_entry['Name'] = student_name
    dict_entry['Section'] = student_section
    dict_entry['Spanish'] = spanish_grade
    dict_entry['English'] = english_grade
    dict_entry['Social Studies'] = social_grade
    dict_entry['Science'] = science_grade
    dict_entry['Average'] = individual_avg
    
    return dict_entry


def input_dict_entry_to_students_list(students_list, dict_entry):
    students_list.append(dict_entry)
    print("\nStudent information entered successfully!")


def ask_if_another_student():
    while True:
        another_student = input("Do you want to enter another student's information? Yes or No: ").upper()

        if another_student in ("YES", "NO"):
            print("\n")
            return another_student
        else:
            print("\nInvalid answer. Please answer Yes or No.")


def create_students_list(students_list):
    while True:
        student_name, student_section = input_student_info()
        spanish_grade, english_grade, social_grade, science_grade = input_grades()
        individual_avg = calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade)
        dict_entry = create_dict_entry(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg)
        input_dict_entry_to_students_list(students_list, dict_entry)

        another_student = ask_if_another_student()
        if another_student == "NO":
            break


def act2_enter_student_into_students_list(students_list):
    create_students_list(students_list)


act2_enter_student_into_students_list(students_list)