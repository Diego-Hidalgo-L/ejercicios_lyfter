

def int_checker(func):
    def wrapper(*args, **kwargs):
        all_params = [*args, *kwargs.values()]
        int_params = []

        for param in all_params:
            try:
                if isinstance(param, int):
                    int_params.append(param)
                else:
                    raise ValueError
            except ValueError:
                print(f"ValueError: '{param}' is not an integer.")

        return func(int_params)
    
    return wrapper


@int_checker
def print_args(*args):
    print("All integer parameters are:")

    for arg in args:
        print(arg)


print_args(1, "hello", 2, "my", 3, "friend", last_param=4)