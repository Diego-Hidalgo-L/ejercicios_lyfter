
from data import read_csv_file_and_extract_students_list, write_csv_file
from menu import show_menu, route_menu_choice


def main():
    students_list = []

    while True:
        menu_choice = show_menu()

        if menu_choice == '10':
            print("Program ended.\n")
            break
        elif menu_choice == '8':
            students_list = read_csv_file_and_extract_students_list('semana_10/proyecto_semana_10/project/students_info.csv')
            print("Data successfully imported!")
        elif menu_choice == '9':
            if not students_list:
                print("No data available. Please import or add student data first.\n")
            else:
                write_csv_file('semana_10/proyecto_semana_10/project/students_info.csv', students_list, students_list[0].keys())
                print("Data successfully exported.")
        else:
            if not students_list:
                print("No data available. Please import student data from CSV file first.\n")
            else:
                route_menu_choice(menu_choice, students_list)


main()