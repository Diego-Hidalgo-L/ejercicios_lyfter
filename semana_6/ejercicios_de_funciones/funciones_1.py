
# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.


def test_function_1():
    print("Hello")
    test_function_2()


def test_function_2():
    print("World!")


test_function_1()