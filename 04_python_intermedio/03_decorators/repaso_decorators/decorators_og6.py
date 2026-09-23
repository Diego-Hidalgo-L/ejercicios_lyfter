
from datetime import date

def log_call(func):
    def wrapper(*args, **kwargs):
        params = [*args, *kwargs.values()]
        result = func(*args, **kwargs)

        print(f"func: {func.__name__} - args: {params} - {date.today()} - resultado: {result}")

        return result

    return wrapper


def validate_numbers(func):
    def wrapper(*args, **kwargs):
        params = [*args, *kwargs.values()]
        valid_params = []

        try:
            for param in params:
                if isinstance(param, int):
                    valid_params.append(param)
                else:
                    raise ValueError(f"El valor '{param}' no es un número")
        except ValueError as e:
            print(e)
        
        return func(*valid_params)

    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(f"Resultado: {result}")
