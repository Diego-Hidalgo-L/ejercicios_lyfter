

def my_function(*args, **kwargs):
    # print(f"First parameter: {first_parameter}")
    print(f"Args: {args}")

    print(f"Kwargs: {kwargs}")


my_function("First value", 1, 2, 3, 4, my_other_parameter="World", whatever=6)