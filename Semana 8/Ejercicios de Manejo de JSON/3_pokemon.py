
import json


def read_json_file_and_return_poke_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        poke_list = json.load(file)
    
    return poke_list


def ask_for_my_pokemon():
    my_pokemon = input("Enter the name of the pokémon you wish to search for: ").capitalize()
    return my_pokemon


def search_poke_list_for_my_pokemon(poke_list, my_pokemon):
    found_my_pokemon = False

    for entry in poke_list:
        name_english = entry.get('name', {}).get('english')
        if my_pokemon == name_english:
            my_pokemon_type = entry.get('type')
            lvl = entry.get('lvl')
            print(f"\n{name_english} (Type: {my_pokemon_type}, Level: {lvl})\n")
            found_my_pokemon = True
    
    if not found_my_pokemon:
        print(f"\n{my_pokemon} isn't on this list.\n")


def main():
    poke_list = read_json_file_and_return_poke_list("pokemon_list.json")
    my_pokemon = ask_for_my_pokemon()
    search_poke_list_for_my_pokemon(poke_list, my_pokemon)


main()