
def validate_number(func):
    def wrapper(*args, **kwargs):
        valid_args = []

        for index, arg in enumerate(args):
            if isinstance(arg, (int, float)):
                valid_args.append(arg)
            else:
                raise TypeError(f"\nArgument {index + 1} ('{arg}') is not a number\n")
            
        return func(*valid_args, **kwargs)
        
    return wrapper


def clamp(min_val, max_val):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if result < min_val:
                print("\nWarning! Result was clamped")
                return min_val
            elif result > max_val:
                print("\nWarning! Result was clamped")
                return max_val
            else:
                return result
        
        return wrapper

    return decorator


@clamp(0, 1_000)
@validate_number
def calculate(*nums):
    result = 1

    for n in nums:
        result *= n

    return result


def main():
    try:
        print(calculate(3, 4, 5))
        print(calculate(5, 5, 5, 5, 5))
        print(calculate(2, 'x', 4))
    except TypeError as e:
        print(str(e))


main()
