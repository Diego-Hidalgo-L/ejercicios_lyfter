
import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = (end - start)

        print(f"{func.__name__} took {elapsed:5f} seconds.")
        return result
    
    return wrapper


@measure_time
def slow_function(x):
    time.sleep(x)


@measure_time
def big_loop(x):
    total = 0

    for number in range(x):
        total += number
    
    return total


def main():
    slow_function(1)
    print(big_loop(1_000_000))


main()