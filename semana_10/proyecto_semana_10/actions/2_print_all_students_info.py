
from semana_10.proyecto_semana_10.students_info import students_list

def print_all_students_info(students_list):
    for student in students_list:
        print(f"{student['Name']} - {student['Section']}")
        print(f"Spanish: {student['Spanish']}")
        print(f"English: {student['English']}")
        print(f"Social Studies: {student['Social Studies']}")
        print(f"Science: {student['Science']}")
        print(f"Overall average: {student['Average']}")
        print("-----------------------")


def main():
    print_all_students_info(students_list)


main()