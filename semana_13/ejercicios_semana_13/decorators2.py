

def int_checker(func):
    def wrapper(*args):

        func(*args)

        for arg in args:
            if isinstance(arg, int):
                print(f"{arg} is an integer.")
            else:
                print(f"{arg} is not an integer.")
    
    return wrapper


@int_checker
def print_args(*args):
    print(args)


print_args(1, "hello", 2, "my", 3, "friend")