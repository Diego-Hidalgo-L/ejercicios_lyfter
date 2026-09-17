
import csv

def read_csv_files(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def main():
    read_csv_files('semana_8/repaso/texto.txt')


main()