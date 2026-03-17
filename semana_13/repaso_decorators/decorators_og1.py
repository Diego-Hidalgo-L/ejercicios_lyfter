
def print_params_and_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        print(f"Los parámetros de la función son: {*args, *kwargs}")
        print(f"El resultado de la función es: {result}")

        return result
    
    return wrapper


@print_params_and_result
def add(a, b):
    return a + b


def main():
    print(add(3, 4))


main()