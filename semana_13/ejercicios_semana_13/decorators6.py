
from datetime import date

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        all_params = [*args, *kwargs.values()]
        valid_params = []

        for param in all_params:
            try:
                if isinstance(param, int):
                    valid_params.append(param)
                else:
                    raise ValueError
            except ValueError:
                print(f"Error:'{param}' is not an integer.")
                continue
        
        print(valid_params)
        return func(*valid_params)
    
    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs.values())
        print(f"func: {func.__name__} - args: {args} - {date.today()} - Resultado: {result}")
        return result

    return wrapper


@validate_numbers
@log_call
def multiply(*args):
    multiplier = 1

    for arg in args:
        multiplier *= arg
    
    print(multiplier)
    return multiplier


multiply(3, "hola", 4)