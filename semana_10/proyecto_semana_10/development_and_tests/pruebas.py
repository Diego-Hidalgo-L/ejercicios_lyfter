
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
    8. Exit.

Please enter a number (1-8) for the action you wish to take: """)

        while True:
            if menu_choice.isdigit() and 1 <= int(menu_choice) <= 8:
                print()
                return menu_choice
            else:
                menu_choice = input("Invalid choice. Please enter a number from 1 to 8: ")
                print()


def route_menu_choice(menu_choice):
    if menu_choice == '1':
        print('1')
    elif menu_choice == '2':
        print('2')
    elif menu_choice == '3':
        print('3')
    elif menu_choice == '4':
        print('4')
    elif menu_choice == '5':
        print('5')
    elif menu_choice == '6':
        print('6')
    elif menu_choice == '7':
        print('7')


def main():
    while True:
        menu_choice = show_menu()

        if menu_choice == '8':
            print("Program stopped.\n")
            break
        route_menu_choice(menu_choice)


main()