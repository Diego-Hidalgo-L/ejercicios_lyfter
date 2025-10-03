
# from students_info import students_list

import csv

# # # # # READER # # # # #

def read_csv_file_and_extract_students_list(path):
    students_list = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_list.append(row)
    
    print(students_list)



# # # # # WRITER # # # # #

def write_csv_file(path, data, headers):
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


# write_csv_file("semana_10/proyecto_semana_10/students_info.csv", students_list, students_list[0].keys())

read_csv_file_and_extract_students_list("semana_10/proyecto_semana_10/students_info.csv")