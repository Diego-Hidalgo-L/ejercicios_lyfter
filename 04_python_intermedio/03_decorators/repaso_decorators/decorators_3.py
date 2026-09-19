
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()
        
        return result

    return wrapper


@uppercase_result
def get_message():
    return "hello world"


@uppercase_result
def get_number():
    return 5

print(get_message())
print(get_number())