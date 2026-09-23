
from functools import wraps
import inspect

def log_signature(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"┌─ Calling: {func.__name__}")

        bound = inspect.signature(func).bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            print(f"| {name} = {value}")
        
        result = func(*args, **kwargs)

        print(f" -> Result: {result}")
        print("└──────────────")

        return result
    
    return wrapper


@log_signature
def add(a, b):
    return a + b


@log_signature
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


@log_signature
def power(base, exponent, mod=None):
    if mod is None:
        return base ** exponent
    return (base ** exponent) % 10


def main():
    add(3, 5)
    print()
    greet("Diego")
    print()
    power(2, 8, 10)
    print()
    power(2, 8)

main()






