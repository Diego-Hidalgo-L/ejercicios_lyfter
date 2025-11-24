

def int_checker(func):
    def wrapper(*args, **kwargs):
        all_params = [*args, *kwargs.values()]

        for param in all_params:
            try:
                if isinstance(param, int):
                    # print(f"{arg} is an integer.")
                    continue
                else:
                    raise ValueError
            except ValueError:
                print(f"ValueError: '{param}' is not an integer.")

        return func(*args, **kwargs)
    
    return wrapper


@int_checker
def print_args(*args, **kwargs):
    print(args, kwargs)


print_args(1, "hello", 2, "my", 3, "friend", last_param=4)