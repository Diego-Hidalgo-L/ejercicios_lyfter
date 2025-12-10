
"""Versión 1"""

def manual_add(number):
    result = 0 # O(1)
    for i in range(1, number + 1): # O(n)
        result += i # O(1)
    return result # O(1)


"""Versión 2"""

def add_formula(number):
    return number * (number + 1) // 2 # O(1)

print(add_formula(1_000_000_000))


"""
Preguntas:

1) ¿Cuál es la complejidad de cada versión?
- Versión 1: O(n)
- Versión 2: O(1)

2) ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
- Usaría la Versión 2, porque es una operación que calcula el resultado directamente. No requiere hacer iteraciones cada vez que se suma un número hasta llegar al número ingresado.
Con la primera versión, entre más grande sea el número, más iteraciones va a realizar. Por ende, entre más grande sea el número ingresado, más tiempo va durar para llegar al resultado.

"""