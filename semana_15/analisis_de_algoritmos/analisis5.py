
def print_all_pairs(my_dict):
    for key1 in my_dict: # O(n)
        for key2 in my_dict: # O(n^2)
            print(f"{key1}-{key2}") # O(1)


"""
Preguntas:

1) ¿Cuál es la complejidad temporal?
- La complejidad temporal es de O(n^2).

2) ¿Cuánto dura si hay 1 millón de claves?
- El algoritmo tendría que realizar 1_000_000_000_000 operaciones.

"""