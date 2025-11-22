
def return_params_and_result(func):
    def wrapper(*args, **kwargs):
        list_of_params = [*args, *kwargs.values()]

        result = func(*args, **kwargs)

        print(f"Parameters: {list_of_params}.")
        print(f"Resultado: {result}")

        return result

    return wrapper


@return_params_and_result
def calculate_area(*args, **kwargs):
    multiplier = 1

    for arg in args:
        multiplier *= arg

    for kwarg in kwargs.values():
        multiplier *= kwarg
    
    return multiplier


print(calculate_area(10, key_param=12))