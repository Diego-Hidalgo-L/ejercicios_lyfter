
import csv

def read_csv_file_and_extract_students_list(path):
    students_list = []
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_list.append(row)
    except FileNotFoundError:
        print("Error: The file does not exist.")

    return students_list


def write_csv_file(path, data, headers):
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)