

def int_checker(func):
    def wrapper(*args):
        for arg in args:
            try:
                if isinstance(arg, int):
                    # print(f"{arg} is an integer.")
                    continue
                else:
                    raise ValueError
            except ValueError:
                print(f"ValueError: '{arg}' is not an integer.")
        
        return func(*args)
    
    return wrapper


@int_checker
def print_args(*args):
    print(args)


print_args(1, "hello", 2, "my", 3, "friend")