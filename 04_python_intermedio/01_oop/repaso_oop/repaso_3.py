
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"{self.name} ({self.species})"
    
    def __repr__(self):
        return f"{self.name!r} ({self.species!r})"


def convert_dict_to_obj(my_list):
    pets_obj = []

    for pet in my_list:
        pets_obj.append(Pet(pet.get("name"), pet.get("species")))
    
    return pets_obj


def print_pets(my_list):
    for pet in my_list:
        print(f"Nombre: {pet.name} - Especie: {pet.species}")


def main():
    pets = [
    {"name": "Firulais", "species": "perro"},
    {"name": "Michi", "species": "gato"}
]
    pets_obj = convert_dict_to_obj(pets)
    print_pets(pets_obj)


main()