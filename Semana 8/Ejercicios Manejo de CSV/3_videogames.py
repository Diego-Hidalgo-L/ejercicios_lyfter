
import csv


def read_file_and_print_rows(path):
    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            for key, value in row.items():
                print(f"{key}: {value}")
            print("------")


def main():
    read_file_and_print_rows("videogames.csv")


main()


# def read_file_and_print_rows(path):
    # with open(path, encoding="utf-8") as file:
        # reader = csv.reader(file)

        # First row of the file contains the headers
        # headers = next(reader)

        # Now pair each row with the headers
        # for row in reader:
            # row_dict = dict(zip(headers, row))
            # for key, value in row_dict.items():
                # print(f"{key}: {value}")
            # print("------")

