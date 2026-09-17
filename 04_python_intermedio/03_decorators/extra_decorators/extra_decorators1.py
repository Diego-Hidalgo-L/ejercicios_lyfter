
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n")
        print(func.__name__)

        if args:
            print(args)
        
        if kwargs:
            print(kwargs)

        result = func(*args, **kwargs)
        print("Resultado: ", result)
        return result
    
    return wrapper


@log_call
def function_1(*args):
    return "".join(args)


@log_call
def function_2(**kwargs):
    all_params = [*kwargs.values()]
    multiplier = 1

    for param in all_params:
        multiplier *= param
    
    return multiplier


def main():
    function_1("Hola, ", "esto ", "es ", "un ", "string.")
    function_2(first_param=12, second_param=4, third_param=5)


main()