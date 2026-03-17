
def limit_calls(limit=3):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls

            if calls >= limit:
                print("Function call limit reached")
                return
            
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