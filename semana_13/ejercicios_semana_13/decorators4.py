

def repeat_twice(func):
    def wrapper(*args, **kwargs):
         return (func(*args, *kwargs.values()), func(*args, *kwargs.values()))

    return wrapper


@repeat_twice
def print_str(name):
    print(f"Hola, {name}")


print_str(my_param="Diego")