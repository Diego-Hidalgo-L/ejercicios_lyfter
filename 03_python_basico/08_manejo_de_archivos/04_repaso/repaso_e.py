
import csv
import json

def read_csv_file(path):
    user_list = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_list.append(row)
    
    return user_list


def write_new_json_file(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    user_list = read_csv_file("semana_8/repaso/usuarios.csv")
    write_new_json_file("semana_8/repaso/usuarios.json", user_list)


main()