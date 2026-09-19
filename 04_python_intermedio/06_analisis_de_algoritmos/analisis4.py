
def linear_search(my_list, target):
    for item in my_list: # O(n)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)


def binary_search(my_list, target):
    low = 0 # O(1)
    high = len(my_list) - 1 # O(1)
    while low <= high: # O(log n) - NO O(n), porque en cada vez se está reduciendo la lista a la mitad.
        mid = (low + high) // 2 # O(1) - Esto lo tenía como O(n) pero fue un error.
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else: # O(1)
            high = mid - 1 # O(1)
    return False # O(1)


"""
Preguntas:

1) ¿Cuál es la complejidad de cada algoritmo?
- linear_search: O(n).
- binary_search: O(log n).

2) ¿En qué condiciones conviene usar cada uno?
- Conviene usar linear_search cuando se tiene una lista no ordenada.
- Conviene usar binary_search cuando la lists sí está ordenada.

3) ¿Qué pasa si la lista no está ordenada?
- Si la lista no está ordenada, no hay forma de que podamos saber si el target se encuentra a la derecha o a la izquierda del midpoint.
El midpoint no nos sirve de referencia.

"""