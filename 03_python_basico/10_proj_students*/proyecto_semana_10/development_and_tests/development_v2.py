
# # # # # Start of MENU # # # # #

def show_menu():
    menu_choice = input("""
Menu options:

    1. View the complete information of all students in the database.            
    2. Enter a new student's information.
    3. Search for a specific student by full name.
    4. Delete a student from the database.
    5. View which students have failing grades.
    6. View the top 3 students as per their grade average.
    7. View the grade average among all the students.
    8. Import all previous data from the CSV file.
    9. Export all modified data into the CSV file.
    10.Exit.

Please enter a number (1-10) for the action you wish to take: """)
    print("\n")
    
    while True:
        if menu_choice.isdigit() and 1 <= int(menu_choice) <= 10:
            return menu_choice
        else:
            menu_choice = input("Invalid choice. Please enter a number from 1 to 10: ")
            print("\n")


def route_menu_choice(menu_choice, students_list):
    if menu_choice == '1':
        act1_print_all_students_info(students_list)
    # act2 is called in main
    elif menu_choice == '3':
        act3_search_for_student(students_list)
    elif menu_choice == '4':
        act4_delete_student(students_list)
    elif menu_choice == '5':
        act5_show_failing_students(students_list)
    elif menu_choice == '6':
        act6_extract_top_3_avgs(students_list)
    elif menu_choice == '7':
        act7_calculate_all_students_avg(students_list)


# # # # # End of MENU # # # # #

# # # # # Start of DATA # # # # #

import csv

import csv

def read_csv_file_and_extract_students_list(path):
    students_list = []
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key, value in row.items():
                    if value.replace('.', '', 1).isdigit():
                        row[key] = float(value)
                students_list.append(row)
    except FileNotFoundError:
        print("Error: The file does not exist.")

    return students_list


def write_csv_file(path, data, headers):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


# # # # # End of DATA # # # # #

# # # # # Start of ACTION 1 # # # # #

def act1_print_all_students_info(students_list):
    for student in students_list:
        print(f"{student['Name']} - {student['Section']}")
        print(f"Spanish: {student['Spanish']}")
        print(f"English: {student['English']}")
        print(f"Social Studies: {student['Social Studies']}")
        print(f"Science: {student['Science']}")
        print(f"Average: {student['Average']}")
        print("------------------------")


# # # # # End of ACTION 1 # # # # #

# # # # # #   Start of ACTION 2   # # # # #

def input_student_section():
    pattern = r"^(1[0-2]|[1-9])[A-Ca-c]$"
    while True:
        student_section = input("Please enter the student's section: ").upper()

        if re.match(pattern, student_section):
            return student_section
        else:
            print("\nInvalid section format. Please try again. ")


import re

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
        if student.get('Name','').lower() == student_name.lower() and student.get('Section','').upper() == student_section.upper():
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


def modify_students_list(students_list):
    while True:
        student_section = input_student_section()
        student_name = input_student_name(students_list, student_section)
        spanish_grade, english_grade, social_grade, science_grade = input_grades()
        individual_avg_rounded = calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade)
        dict_entry = create_dict_entry(student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg_rounded)
        input_dict_entry_to_students_list(students_list, dict_entry)

        another_student = ask_if_another_student()
        if another_student == "NO":
            break


def act2_enter_student_into_students_list(students_list):
    modify_students_list(students_list)


# # # # # # End of ACTION 2 # # # # #

# # # # # Start of ACTION 3 # # # # #

def ask_for_student_to_search():
    student_to_search = input("Enter the name of the student you want to search for: ").strip().title()

    return student_to_search


def search_student_through_list(student_to_search, students_list):
    for student in students_list:
        if student_to_search == student.get('Name'):
            print(f"\n{student['Name']} - {student['Section']}")
            print(f"Spanish: {student['Spanish']}")
            print(f"English: {student['English']}")
            print(f"Social Studies: {student['Social Studies']}")
            print(f"Science: {student['Science']}")
            print(f"Average: {student['Average']}\n")
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
    for i, student in enumerate(students_list):
        if student_to_delete == student.get('Name'):
            students_list.pop(i)
            print(f"\n{student.get('Name')} was deleted from the database.\n")
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
        failing_student_dict = {'Name': student.get('Name'), 'Section': student.get('Section'), 'Average': student.get('Average')}
        for subject, value in student.items():
            if subject not in ("Name", "Section", "Average"): 
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
    sorted_students = sorted(students_list, key=lambda s: float(s['Average']), reverse=True)
    top_three = sorted_students[:3]

    print("The students with the top three average grades are: ")
    for student in top_three:
        print(f"{student['Name']}")
        print(f"Average: {student.get('Average')}")
        print("----------------")


# # # # # End of ACTION 6 # # # # #

# # # # # Start of ACTION 7 # # # # #

def act7_calculate_all_students_avg(students_list):
    sum_of_avgs = 0
    for student in students_list:
        ind_avg = float(student.get('Average'))
        sum_of_avgs += ind_avg
    
    all_students_avg = sum_of_avgs / len(students_list)

    print (f"The overall average grade among all students is: {all_students_avg:.2f}\n")


# # # # # End of ACTION 7 # # # # #

# # # # # Start of MAIN # # # # #

def main():
    students_list = []

    while True:
        menu_choice = show_menu()

        if menu_choice == '10':
            print("Program ended.\n")
            break
        elif menu_choice == '8':
            students_list = read_csv_file_and_extract_students_list('semana_10/proyecto_semana_10/project/students_info.csv')
            if students_list:
                print("Data successfully imported!")
            else:
                print("No data imported.")
        elif menu_choice == '9':
            if not students_list:
                print("No data available. Please import or add student data first.\n")
            else:
                write_csv_file('semana_10/proyecto_semana_10/project/students_info.csv', students_list, students_list[0].keys())
                print("Data successfully exported!")
        elif menu_choice == '2':
            act2_enter_student_into_students_list(students_list)
        else:
            if not students_list:
                print("No data available. Please import student data from CSV file first.\n")
            else:
                route_menu_choice(menu_choice, students_list)


main()