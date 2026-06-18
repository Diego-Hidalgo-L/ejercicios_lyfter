
import time
from functools import wraps

def make_logger(prefix, **log_options):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} | Calling: {func.__name__} | Args: {args} | Kwargs: {kwargs}")

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            
            elapsed = end - start

            if log_options.get('log_result', False):
                print(f"{prefix} | Result: {result}")
            
            if log_options.get('log_time', False):
                print(f"{prefix} | Time elapsed: {elapsed:.4f}s")
            
            return result
        
        return wrapper
    
    return decorator


@make_logger("APP", log_result=True, log_time=True)
def multiply(*nums):
    result = 1

    for n in nums:
        result *= n

    return result


multiply(3, 4, 5)