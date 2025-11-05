from data import Student

# # # # # Start of ACTION 1 # # # # #

def act1_print_all_students_info(students_list):
    for student in students_list:
        print(f"{student.student_name} - {student.student_section}")
        print(f"Spanish: {student.spanish_grade}")
        print(f"English: {student.english_grade}")
        print(f"Social Studies: {student.social_grade}")
        print(f"Science: {student.science_grade}")
        print(f"Average: {student.individual_avg}")
        print("------------------------")


# # # # # End of ACTION 1 # # # # #

# # # # # Start of ACTION 2 # # # # #

import re

def input_student_section():
    pattern = r"^(1[0-2]|[1-9])[A-Ca-c]$"
    while True:
        student_section = input("Please enter the student's section: ").upper()

        if re.match(pattern, student_section):
            return student_section
        else:
            print("\nInvalid section format. Please try again. ")


def is_valid_name(prompt):
    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-' ][A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    while True:
        name = input(prompt).strip().title()
        if not name:
            print("\nThis field can't be empty. Please enter the student's name.\n")
        elif not re.match(pattern, name):
            print("\nInvalid input. The name can't have any numbers or special characters.\n")
        else:
            return name


def student_exists(student_name, student_section, students_list):
    for student in students_list:
        if student.student_name.lower() == student_name.lower() and student.get('Section','').upper() == student_section.upper():
            return True
    return False


def input_student_name(students_list, student_section):
    while True:
        student_name = is_valid_name("Please enter the student's name: ")
        if student_exists(student_name, student_section, students_list):
            print(f"\n'{student_name}' is already in the database.\n")
        else:
            return student_name


def validate_grade(prompt):
    while True:
        grade = input(prompt)
        try:
            valid_grade = float(grade)
            if 0 <= valid_grade <= 100:
                return valid_grade
            else:
                print("\nInvalid answer. Please enter a grade from 0 to 100.")
        except ValueError:
            print("\nInvalid answer. Please enter a valid number.")


def input_grades():
    spanish_grade = validate_grade("Please enter the student's Spanish grade: ")
    english_grade = validate_grade("Please enter the student's English grade: ")
    social_grade = validate_grade("Please enter the student's Social Studies grade: ")
    science_grade = validate_grade("Please enter the student's Science grade: ")

    return spanish_grade, english_grade, social_grade, science_grade


def calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade): # Optimize to not be limited to just 4 subjects
    individual_avg = (spanish_grade + english_grade + social_grade + science_grade) / 4
    individual_avg_rounded = round(individual_avg, 2)

    return individual_avg_rounded


        # Change this from a dictionary into an object #

def create_student_obj(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg):
    student_obj = Student(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg)
    return student_obj


def input_student_obj_to_students_list(students_list, student_obj):
    students_list.append(student_obj)
    print("\nStudent information entered successfully!")

        # Change this from a dictionary into an object #

def ask_if_another_student():
    while True:
        another_student = input("Do you want to enter another student's information? Yes or No: ").upper()

        if another_student in ("YES", "NO"):
            print("\n")
            return another_student
        else:
            print("\nInvalid answer. Please answer Yes or No.")


def modify_students_list(students_list):
    while True:
        student_section = input_student_section()
        student_name = input_student_name(students_list, student_section)
        spanish_grade, english_grade, social_grade, science_grade = input_grades()
        individual_avg = calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade)
        student_obj = create_student_obj(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg)
        input_student_obj_to_students_list(students_list, student_obj)

        another_student = ask_if_another_student()
        if another_student == "NO":
            break


def act2_enter_student_into_students_list(students_list):
    modify_students_list(students_list)


# # # # # End of ACTION 2 # # # # #

# # # # # Start of ACTION 3 # # # # #

def ask_for_student_to_search():
    student_to_search = input("Enter the name of the student you want to search for: ").strip().title()

    return student_to_search


def search_student_through_list(student_to_search, students_list):
    for student in students_list:
        if student_to_search == student.student_name:
            print(f"\n{student.student_name} - {student.student_section}")
            print(f"Spanish: {student.spanish_grade}")
            print(f"English: {student.english_grade}")
            print(f"Social Studies: {student.social_grade}")
            print(f"Science: {student.science_grade}")
            print(f"Average: {student.individual_avg}\n")
            break
    else:
        print(f"\nNo student named '{student_to_search}' was found.\n")


def act3_search_for_student(students_list):
    student_to_search = ask_for_student_to_search()
    search_student_through_list(student_to_search, students_list)


# # # # # End of ACTION 3 # # # # #

# # # # #  Start of ACTION 4 # # # # #

def ask_for_student_to_delete():
    student_to_delete = input("Enter the name of the student you want to delete: ").strip().title()

    return student_to_delete


def delete_student_from_students_list(student_to_delete, students_list):
    for student in students_list:
        if student_to_delete == student.student_name:
            students_list.remove(student)
            print(f"\n{student.student_name} was deleted from the database.\n")
            break

    else:
        print(f"\nNo student named '{student_to_delete}' was found.\n")


def ask_for_confirmation(student_to_delete, students_list):
    while True:
        confirm = input(f"\nAre you sure you want to delete {student_to_delete}'s information? Yes or No: ").upper()

        if confirm in ("YES", "NO"):
            if confirm == "YES":
                delete_student_from_students_list(student_to_delete, students_list)
                break
            elif confirm == "NO":
                # print("\nThen what the fuck?\n")
                break
        else:
            print("\nInvalid answer. Please answer either Yes or No.\n")


def act4_delete_student(students_list):
    student_to_delete = ask_for_student_to_delete()
    ask_for_confirmation(student_to_delete, students_list)

# # # # #  End of ACTION 4 # # # # #

# # # # # Start of ACTION 5 # # # # #

def search_for_failing_grades(students_list):
    failing_students_list = []

    for student in students_list:
        failing_student_dict = {'Name': student.student_name, 'Section': student.student_section, 'Average': student.individual_avg}
        grades_dict = {'Spanish': student.spanish_grade, 'English': student.english_grade, 'Social Studies': student.social_grade, 'Science': student.science_grade}

        for subject, value in grades_dict.items():
            try:
                grade = float(value)
                if grade < 60:
                    failing_student_dict[subject] = grade
            except ValueError:
                continue

        if len(failing_student_dict) > 3:
                failing_students_list.append(failing_student_dict)

    return failing_students_list


def iterate_through_failing_students_list(failing_students_list):
    print("The students with failing grades are:\n")
    if failing_students_list == []:
        print("There are no failing students.\n")
        return

    else:
        print(f"There are {len(failing_students_list)} students with failing grades:")
        for student in failing_students_list:
            print(f"{student['Name']} - {student['Section']}")
            for subject, grade in student.items():
                if subject not in ("Name", "Section", "Average"):
                    print(f"{subject}: {grade}")
            print(f"Average: {student.get('Average')}")
            print("--------------------")


def act5_show_failing_students(students_list):
    failing_students_list = search_for_failing_grades(students_list)
    iterate_through_failing_students_list(failing_students_list)

# # # # # End of ACTION 5 # # # # #

# # # # # Start of ACTION 6 # # # # #

def act6_extract_top_3_avgs(students_list):
    sorted_students = sorted(students_list, key=lambda s: float(s.individual_avg), reverse=True)
    top_three = sorted_students[:3]

    print("The students with the top three average grades are: ")
    for student in top_three:
        print(f"{student.student_name}")
        print(f"Average: {student.individual_avg}")
        print("----------------")


# # # # # End of ACTION 6 # # # # #

# # # # # Start of ACTION 7 # # # # #

def act7_calculate_all_students_avg(students_list):
    sum_of_avgs = 0
    for student in students_list:
        ind_avg = float(student.individual_avg)
        sum_of_avgs += ind_avg
    
    all_students_avg = sum_of_avgs / len(students_list)

    print (f"The overall average grade among all students is: {all_students_avg:.2f}\n")


# # # # # End of ACTION 7 # # # # #