
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

def main():
    students_list = read_csv_file_and_extract_students_list('semana_10/proyecto_semana_10/project/students_info.csv')
    print(students_list)


main()