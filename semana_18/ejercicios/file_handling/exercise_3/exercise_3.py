
import csv

def input_game_info():
    name = input("Name: ").title()
    genre = input("Genre: ").title()
    developer = input("Developer: ").title()

    return name, genre, developer


def input_esrb_rating():
    ratings = ['E', 'T', 'M', 'AO']

    while True:
        esrb_rating = input("ESRB rating: ").upper()

        if esrb_rating not in ratings:
            print("Error: Please enter a valid rating (E, T, M, AO)")
            continue

        return esrb_rating


def input_release_year():
    while True:
        release_year = int(input("Release year: "))

        if not 1970 <= release_year <= 2026:
            print("Error: Please enter a valid release year (1970-2026)")
            continue

        return release_year


def input_metacritic_score():
    while True:
        score = int(input("Metacritic score: "))

        if not 0 <= score <= 100:
            print("Error: Please enter a valid Metacritic score (0-100)")
            continue

        return score


def create_dict_entry(name, genre, developer, esrb_rating, release_year, score):
    dict_entry = {}
    
    dict_entry['Name'] = name
    dict_entry['Genre'] = genre
    dict_entry['Developer'] = developer
    dict_entry['ESRB rating'] = esrb_rating
    dict_entry['Release year'] = release_year
    dict_entry['Metacritic score'] = score
    
    return dict_entry


def input_dict_entry_to_games_list(games_list, dict_entry):
    games_list.append(dict_entry)
    print("\nVideogame entered successfully!")


def ask_if_go_on():
    while True:
        try:
            go_on = input("Do you want to enter another game? Yes or No: ")
            go_on = go_on.lower()

            if go_on == "yes" or go_on == "no":
                print("\n")
                return go_on
            else:
                raise ValueError
        except ValueError:
            print("Invalid response. Please enter Yes or No")


def create_games_list():
    games_list = []

    while True:
        name, genre, developer = input_game_info()
        esrb_rating = input_esrb_rating()
        release_year = input_release_year()
        score = input_metacritic_score()
        dict_entry = create_dict_entry(name, genre, developer, esrb_rating, release_year, score)
        input_dict_entry_to_games_list(games_list, dict_entry)
        
        go_on = ask_if_go_on()
        if go_on == "no":
            break

    return games_list


def read_csv_file(path):
    with open(path, encoding='utf-8') as file:
        return csv.DictReader(file)


def overwrite_csv_file(path, data, headers):
    with open(path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def append_to_csv_file(path, data, headers):
    with open(path, 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerows(data)


def main():
    games_list = create_games_list()
    reader = read_csv_file("semana_18/ejercicios/file_handling/exercise_3/videogames.csv")

    if reader:
        append_to_csv_file("semana_18/ejercicios/file_handling/exercise_3/videogames.csv", games_list, games_list[0].keys())
    else:
        overwrite_csv_file("semana_18/ejercicios/file_handling/exercise_3/videogames.csv", games_list, games_list[0].keys())


main()