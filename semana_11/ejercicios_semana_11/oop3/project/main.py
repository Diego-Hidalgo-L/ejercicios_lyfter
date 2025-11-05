from menu import show_menu, route_menu_choice
from data import read_csv_file_and_extract_students_list, write_csv_file
from actions import act2_enter_student_into_students_list

def main():
    students_obj_list = []
    headers = ["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]

    while True:
        menu_choice = show_menu()

        if menu_choice == '10':
            print("Program ended.\n")
            break
        elif menu_choice == '8':
            students_obj_list = read_csv_file_and_extract_students_list('semana_11/ejercicios_semana_11/oop3/project/students_info.csv', students_obj_list)
            if students_obj_list:
                print("Data successfully imported!")
            else:
                print("No data imported.")
        elif menu_choice == '9':
            if not students_obj_list:
                print("No data available. Please import or add student data first.\n")
            else:
                write_csv_file('semana_11/ejercicios_semana_11/oop3/project/students_info.csv', students_obj_list, headers)
                print("Data successfully exported!")
        elif menu_choice == '2':
            act2_enter_student_into_students_list(students_obj_list)
        else:
            if not students_obj_list:
                print("No data available. Please import student data from CSV file first.\n")
            else:
                route_menu_choice(menu_choice, students_obj_list)


main()