
def repeat_twice(func):
    def wrapper(*args, **kwargs):
        return (func(*args, **kwargs), func(*args, **kwargs))
    
    return wrapper


@repeat_twice
def greet(name):
    print(f"Hola, {name}")


def main():
    greet("Diego")


main()
