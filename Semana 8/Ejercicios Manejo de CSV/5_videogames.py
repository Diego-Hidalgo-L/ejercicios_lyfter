
import csv


def read_file_and_create_genres_dict(path):
    genres_dict = {}

    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            genre = row.get("Género")
            if genre not in genres_dict:
                genres_dict[f"{genre}"] = 1
            else:
                genres_dict[f"{genre}"] += 1
    
    return genres_dict


def print_genres(genres_dict):
    for genre, value in genres_dict.items():
        print(f"{genre}: {value}")


def main():
    genres_dict = read_file_and_create_genres_dict("videogames.csv")

    print("\nGéneros encontrados:")
    print_genres(genres_dict)


main()