
import json


def read_json_file_and_return_poke_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        my_poke_list = json.load(file)
    
    return my_poke_list


def ask_for_poke_type(pokemon_types_list):
    while True:
        my_poke_type = input("Enter the type of pokémon you want to search for: ").capitalize()
        if my_poke_type in pokemon_types_list:
            return my_poke_type
        elif my_poke_type not in pokemon_types_list:
            print("\n")
            print("Invalid answer. Please enter a valid pokémon type.")


def search_for_poke_type(my_poke_list, my_poke_type):
    found_type = False

    print(f"\nAll {my_poke_type}-type pokémon on the list are: ")
    for entry in my_poke_list:
        poke_type = entry.get('type')


        if my_poke_type in poke_type:
            poke_name_english = entry.get('name', {}).get('english')
            print(poke_name_english)
            found_type = True

    if not found_type:
        print(f"There are no {my_poke_type}-type pokémon on this list.")
    print("\n")


def main():
    pokemon_types_list = [
    "Normal",
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy"
]

    my_poke_list = read_json_file_and_return_poke_list("pokemon_list.json")
    my_poke_type = ask_for_poke_type(pokemon_types_list)
    search_for_poke_type(my_poke_list, my_poke_type)


main()