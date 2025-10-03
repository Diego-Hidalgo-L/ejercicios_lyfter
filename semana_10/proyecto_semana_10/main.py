
# # # # # Start of MENU # # # # #

def show_menu():
    menu_choice = input("""
Menu options:
                        
    1. Enter a new student's information.
    2. See the complete information of all entered students.
    3. See the top 3 students as per their average.
    4. See the average score among all the students.
    5. Export all current data into CSV file.
    6. Import all current data from previously exported CSV file.

Please enter the correct option for the action you wish to take: """)
    print("\n")
    return menu_choice


def route_menu_choice(menu_choice):
    if menu_choice == '1':
        act1_enter_student_into_students_list()
    elif menu_choice == '2':
        act2_print_all_students_info(students_list)
    elif menu_choice == '3':
        act3_extract_top_3_avgs(students_list)
    elif menu_choice == '4':
        act4_calculate_all_students_avg(students_list)


# # # # # End of MENU # # # # #



# # # # # #   Start of ACTION 1   # # # # #

# Para hacer esto bien, necesito:
    # 1) Abrir un archivo CSV;
    # 2) Descargar la lista de estudiantes que ese archivo contiene;
    # 3) Append la información de ese nuevo estudiante a la lista;
    # 4) Reescribir el archivo CSV y guardarlo.

import csv

def read_csv_file_and_extract_students_list(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        print(reader)


def input_student_info():
    student_name = input("Please enter the student's full name: ") # Tiene que hacerse mayuscula solo.
    student_section = input("Please enter the student's section: ")
    
    return student_name, student_section


def validate_score_number(prompt):
    while True:
        number = input(prompt)
        try:
            valid_number = float(number)
            if 1 <= valid_number <= 100:
                return valid_number
            else:
                print("\nInvalid answer. Please enter a score from 1 to 100.")
        except ValueError:
            print("\nInvalid answer. Please enter a valid number.")


def input_scores():
    spanish_score = validate_score_number("Please enter the student's Spanish score: ")
    english_score = validate_score_number("Please enter the student's English score: ")
    social_score = validate_score_number("Please enter the student's Social Studies score: ")
    science_score = validate_score_number("Please enter the student's Science score: ")

    return spanish_score, english_score, social_score, science_score


def calculate_individual_avg(spanish_score, english_score, social_score, science_score): # optimize to not be limited to just 4 subjects
    individual_avg = (spanish_score + english_score + social_score + science_score) / 4

    return individual_avg


def create_dict_entry(student_name, student_section, spanish_score, english_score, social_score, science_score, individual_avg):
    dict_entry = {}
    
    dict_entry['Name'] = student_name
    dict_entry['Section'] = student_section
    dict_entry['Spanish'] = spanish_score
    dict_entry['English'] = english_score
    dict_entry['Social Studies'] = social_score
    dict_entry['Science'] = science_score
    dict_entry['Average'] = individual_avg
    
    return dict_entry


def input_dict_entry_to_students_list(students_list, dict_entry):
    students_list.append(dict_entry)
    print("\nStudent information entered successfully!")


def ask_if_another_student():
    while True:
        try:
            another_student = input("Do you want to enter another student's information? Yes or No: ").upper()

            if another_student == "YES" or another_student == "NO":
                print("\n")
                return another_student
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid answer. Please answer Yes or No.")


def create_students_list():
    students_list = []

    while True:
        student_name, student_section = input_student_info()
        spanish_score, english_score, social_score, science_score = input_scores()
        individual_avg = calculate_individual_avg(spanish_score, english_score, social_score, science_score)
        dict_entry = create_dict_entry(student_name, student_section, spanish_score, english_score, social_score, science_score, individual_avg)
        input_dict_entry_to_students_list(students_list, dict_entry)
        
        another_student = ask_if_another_student()
        if another_student == "NO":
            break

    return students_list


def act1_enter_student_into_students_list():
    students_list = create_students_list()
    print("Action 1 completed.")

# # # # # #   End of ACTION 1   # # # # #



# # # # # Start of ACTION 2 # # # # #

def act2_print_all_students_info(students_list):
    for student in students_list:
        print(f"{student['Name']} - {student['Section']}")
        print(f"Spanish: {student['Spanish']}")
        print(f"English: {student['English']}")
        print(f"Social Studies: {student['Social Studies']}")
        print(f"Science: {student['Science']}")
        print(f"Average: {student['Average']}")
        print("------------------------")

# # # # # End of ACTION 2 # # # # #



# # # # # Start of ACTION 3 # # # # #

def act3_extract_top_3_avgs(students_list):
    sorted_students = sorted(students_list, key=lambda s: s['Average'], reverse=True)
    top_three = sorted_students[:3]

    print("The students with the top three average scores are: ")
    for student in top_three:
        print(f"{student['Name']}")
        print(f"Average: {student['Average']}")
        print("----------------")

# # # # # End of ACTION 3 # # # # #



# # # # # Start of ACTION 4 # # # # #

def act4_calculate_all_students_avg(students_list):
    sum_of_avgs = 0
    for student in students_list:
        ind_avg = student['Average']
        sum_of_avgs += ind_avg
    
    all_students_avg = sum_of_avgs / len(students_list)

    print (f"The overall average score among all students is: {all_students_avg}\n")

# # # # # End of ACTION 4 # # # # #



# # # # # Start of MAIN # # # # #

from students_info import students_list # Eliminar esto una vez que se haya terminado la base del código!

def main():
    menu_choice = show_menu()
    route_menu_choice(menu_choice)


main()