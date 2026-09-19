
import csv

# -------- START: Add new game --------

def input_game_info():
    name = input("Name: ").title()
    genre = input("Genre: ").title()
    developer = input("Developer: ").title()

    return name, genre, developer


def input_esrb_rating(ratings):
    while True:
        esrb_rating = input("ESRB rating: ").upper()

        if esrb_rating not in ratings:
            print("Error: Please enter a valid rating (E, T, M, AO)")
            continue

        return esrb_rating


def input_release_year():
    while True:
        try:
            release_year = int(input("Release year: "))

            if not 1970 <= release_year <= 2026:
                print("Error: Please enter a valid release year (1970-2026)")
                continue

            return release_year
        
        except ValueError:
            print("Error: Please enter a year in numbers")
            continue


def input_metacritic_score():
    while True:
        try:
            score = int(input("Metacritic score: "))

            if not 0 <= score <= 100:
                print("Error: Please enter a valid Metacritic score (0-100)")
                continue

            return score

        except ValueError:
            print("Please enter a valid score")
            continue


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


def create_games_list(RATINGS):
    games_list = []

    while True:
        name, genre, developer = input_game_info()
        esrb_rating = input_esrb_rating(RATINGS)
        release_year = input_release_year()
        score = input_metacritic_score()
        dict_entry = create_dict_entry(name, genre, developer, esrb_rating, release_year, score)
        input_dict_entry_to_games_list(games_list, dict_entry)
        
        go_on = ask_if_go_on()
        if go_on == "no":
            break

    return games_list

# -------- END: Add new game --------

# -------- START: CSV handling --------

def file_exists(path):
    try:
        with open(path, 'r', encoding='utf-8'):
            return True
    except FileNotFoundError:
        return False


def overwrite_csv_file(path, data, headers):
    with open(path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def append_to_csv_file(path, data, headers):
    with open(path, 'a', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerows(data)

# -------- END: CSV handling --------

# -------- START: Display all games --------

def display_all_games(path):
    try:
        with open(path, 'r',  encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                for key, value in row.items():
                    print(f"{key}: {value}")
                print("-------------------")

    except FileNotFoundError:
        print("No games file found yet. Add some games first.")

# -------- END: Display all games --------

# -------- START: Filter by ESRB rating --------

def filter_by_rating(RATINGS, path):
    while True:
        rating = input("\nSearch ESRB rating: ").upper()
        print()

        if rating not in RATINGS:
            print("Please enter a valid rating (E, T, M, AO)")
            continue

        break

    try:
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rating_found = False

            for row in reader:
                if row['ESRB rating'] == rating:
                    rating_found = True

                    for key, value in row.items():
                        print(f"{key}: {value}")
                    print("-------------------")
            
            if not rating_found:
                print(f"There are no games with that rating ({rating}).")
    
    except FileNotFoundError:
        print("No games file found yet. Add some games first.")

# -------- END: Filter by ESRB rating --------

# -------- START: Filter by developer --------

def filter_by_developer(path):
    developer = input("\nSearch for developer: ").title()
    print()

    try:
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            developer_found = False

            for row in reader:
                if row['Developer'] == developer:
                    developer_found = True

                    for key, value in row.items():
                        print(f"{key}: {value}")
                    print("-------------------")

            if not developer_found:
                print(f"There are no games by that developer ({developer})")
    
    except FileNotFoundError:
        print("No games file found yet. Add some games first.")

# -------- END: Filter by developer --------

# -------- START: Count games per genre --------

def count_games_per_genre(path):
    genre_dict = {}

    try:
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                genre = row['Genre']

                if genre in genre_dict:
                    genre_dict[genre] += 1
                else:
                    genre_dict[genre] = 1
    
    except FileNotFoundError:
        print("No games file found yet. Add some games first.")
    
    sorted_dict = dict(sorted(genre_dict.items(), key=lambda item: item[1], reverse=True))

    print()
    for game, count in sorted_dict.items():
        print(f"{game}: {count}")
        print("-------------")

# -------- END: Count games per genre --------

# -------- START: Find highest-rated per genre --------

def find_highest_rated(path):
    highest_per_genre = {}

    try:
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                genre = row['Genre']
                score = int(row['Metacritic score'])

                if genre not in highest_per_genre:
                    highest_per_genre[genre] = row

                elif score > int(highest_per_genre[genre]['Metacritic score']):
                    highest_per_genre[genre] = row

    except FileNotFoundError:
        print("No games file found yet. Add some games first.")
    
    for genre, game in highest_per_genre.items():
        print(f"{genre}: {game['Name']} ({game['Metacritic score']})")
        print("--------------------------------")


# -------- END: Find highest-rated per genre --------

# -------- START: Menu--------

def menu():
    print("""
Menu:
1) Add video game.
2) Display all games.
3) Filter games by ESRB rating.
4) Filter games by developer.
5) Count games per genre.
6) Find highest-rated game per genre.
""")
    
    while True:
        try:
            option = int(input("Please select an option: "))

            if option not in range(1, 7):
                print("Please enter a number from 1 to 6")
                continue

            return option
        
        except ValueError:
            print("Please enter a valid number")

# -------- END: Menu--------


# -------- START: Main--------

def main():
    RATINGS = ['E', 'T', 'M', 'AO']
    csv_exists = file_exists("semana_18/ejercicios/file_handling/exercise_3/games.csv")
    option = menu()

    if option == 1:
        print("\nAdding new game:")
        games_list = create_games_list(RATINGS)

        if csv_exists:
            append_to_csv_file("semana_18/ejercicios/file_handling/exercise_3/games.csv", games_list, games_list[0].keys())
        else:
            overwrite_csv_file("semana_18/ejercicios/file_handling/exercise_3/games.csv", games_list, games_list[0].keys())

    elif option == 2:
        display_all_games("semana_18/ejercicios/file_handling/exercise_3/games.csv")
    
    elif option == 3:
        filter_by_rating(RATINGS, "semana_18/ejercicios/file_handling/exercise_3/games.csv")
    
    elif option == 4:
        filter_by_developer("semana_18/ejercicios/file_handling/exercise_3/games.csv")

    elif option == 5:
        count_games_per_genre("semana_18/ejercicios/file_handling/exercise_3/games.csv")

    elif option == 6:
        find_highest_rated("semana_18/ejercicios/file_handling/exercise_3/games.csv")

main()