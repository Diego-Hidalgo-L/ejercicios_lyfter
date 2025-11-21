

def repeat_twice(func):
    def wrapper(name):
        func(name)
        func(name)
    
    return wrapper


@repeat_twice
def print_str(name):
    print(f"Hola, {name}")


print_str("Diego")