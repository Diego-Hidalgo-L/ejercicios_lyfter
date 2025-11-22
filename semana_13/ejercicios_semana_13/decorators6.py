
from datetime import date

def log_call(func):
    def wrapper(*args):
        result = func(*args)
        print(f"func: {func.__name__} - args: {args} - {date.today()} - Resultado: {result}")
        return result

    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, int):
                    continue
            else:
                print(f"Error:'{arg}' is not an integer.")
                return None
        
        return func(*args)
    
    return wrapper


@log_call
@validate_numbers
def multiply(*args):
    multiplier = 1

    for arg in args:
        multiplier *= arg
        
    return multiplier


multiply(3, "hola", 4)