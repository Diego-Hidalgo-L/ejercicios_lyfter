
from actions import (
    act1_print_all_students_info,
    act3_search_for_student,
    act4_delete_student,
    act5_show_failing_students,
    act6_extract_top_3_avgs,
    act7_calculate_all_students_avg
)

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
    # act2 is called in main.py
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