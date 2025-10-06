
from data import read_csv_file_and_extract_students_list, write_csv_file
from menu import show_menu, route_menu_choice


def main():
    students_list = read_csv_file_and_extract_students_list("semana_10/proyecto_semana_10/students_info.csv")
    menu_choice = show_menu()
    route_menu_choice(menu_choice, students_list)
    write_csv_file("semana_10/proyecto_semana_10/students_info.csv", students_list, students_list[0].keys())


main()