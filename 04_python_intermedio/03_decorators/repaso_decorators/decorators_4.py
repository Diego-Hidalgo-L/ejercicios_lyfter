
def limit_calls(limit=3):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls

            if calls >= limit:
                return f"Function call limit reached"
            
            calls += 1
            return func(*args, **kwargs)
    
        return wrapper
    
    return decorator


@limit_calls(3)
def say_hi():
    print("Hi")

say_hi()
say_hi()
say_hi()
say_hi()