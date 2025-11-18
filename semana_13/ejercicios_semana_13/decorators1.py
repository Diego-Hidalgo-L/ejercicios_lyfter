
def return_params_and_result(func):
    def wrapper(width, length):
        result = func(width, length)
        print(f"Parameters: {width, length}.")
        print(result)

    return wrapper


@return_params_and_result
def calculate_area(width, length):
    return width * length


calculate_area(10,12)