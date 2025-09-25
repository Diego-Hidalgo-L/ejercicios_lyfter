
def input_poke_name(pokemon_entry):
    poke_name = input("Please enter the pokémon's name: ").capitalize()
    pokemon_entry['name'] = {'english': f'{poke_name}'}
    
    return pokemon_entry


def input_poke_lvl(pokemon_entry):
    while True:
        try:
            poke_lvl = int(input("Please enter the level of your pokémon: "))
            if 1 <= poke_lvl <= 100:
                pokemon_entry['lvl'] = poke_lvl
                return pokemon_entry
            else:
                print("Level must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def ask_if_add_other_type():
    while True:
        add_other_type = input("Do you want to enter another type? Yes or No: ").upper()

        if add_other_type == "YES" or add_other_type == "NO":
            print("\n")
            return add_other_type
        else:
            print("Invalid answer. Please enter either Yes or No.")


def input_poke_type(pokemon_entry, pokemon_types_list):
    my_poke_type_list = []

    while True:
        poke_type = input("Please enter the pokémon's type: ").capitalize()

        if poke_type in pokemon_types_list:
            if poke_type not in my_poke_type_list:
                my_poke_type_list.append(poke_type)
                print("\nPokémon type entered successfully!")
                
                if len(my_poke_type_list) == 2:
                    pokemon_entry['type'] = my_poke_type_list
                    break

            else:
                print("\nThis type has already been entered.")

            add_other_type = ask_if_add_other_type()
            if add_other_type == "NO":
                pokemon_entry['type'] = my_poke_type_list
                break

        else:
            print("Invalid answer. Please enter a valid pokémon type.")

    return pokemon_entry


def input_poke_base(pokemon_entry):
    while True:
        try:
            poke_base = {}
            poke_base["HP"] = int(input("Enter the Pokémon's HP stat: "))
            poke_base["Attack"] = int(input("Enter the Pokémon's Attack stat: "))
            poke_base["Defense"] = int(input("Enter the Pokémon's Defense stat: "))
            poke_base["Sp. Attack"] = int(input("Enter the Pokémon's Sp. Attack stat: "))
            poke_base["Sp. Defense"] = int(input("Enter the Pokémon's Sp. Defense stat: "))
            poke_base["Speed"] = int(input("Enter the Pokémon's Speed stat: "))

            pokemon_entry["base"] = poke_base
            return pokemon_entry   

        except ValueError:
            print("Invalid input. Please enter numbers only for all stats.")


def create_pokemon_entry():
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
    pokemon_entry = {}

    pokemon_entry = input_poke_name(pokemon_entry)
    pokemon_entry = input_poke_lvl(pokemon_entry)
    pokemon_entry = input_poke_type(pokemon_entry, pokemon_types_list)
    pokemon_entry = input_poke_base(pokemon_entry)

    return pokemon_entry


import json


def read_json_file_and_create_poke_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        poke_list = json.load(file)

        return poke_list


def append_pokemon_entry_to_poke_list(poke_list, pokemon_entry):
    poke_list.append(pokemon_entry)

    return poke_list


def write_pokemon_entry_into_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pokemon_entry = create_pokemon_entry()
    poke_list = read_json_file_and_create_poke_list("pokemon_list.json")
    poke_list = append_pokemon_entry_to_poke_list(poke_list, pokemon_entry)
    write_pokemon_entry_into_json_file("pokemon_list.json", poke_list)


main()