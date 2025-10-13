
students_list = []

def act1_print_all_students_info(students_list):
    if not students_list:
        print("There is no student data.\n")
    else:
        for student in students_list:
            print(f"{student['Name']} - {student['Section']}")
            print(f"Spanish: {student['Spanish']}")
            print(f"English: {student['English']}")
            print(f"Social Studies: {student['Social Studies']}")
            print(f"Science: {student['Science']}")
            print(f"Average: {student['Average']}")
            print("------------------------")


act1_print_all_students_info(students_list)