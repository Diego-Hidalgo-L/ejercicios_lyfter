
def return_area(func):
    def wrapper(width, length):
        result = func(width, length)
        print(f"Parameters: {width, length}.")
        print(result)

    return wrapper


@return_area
def calculate_area(width, length):
    return width * length


calculate_area(10,12)