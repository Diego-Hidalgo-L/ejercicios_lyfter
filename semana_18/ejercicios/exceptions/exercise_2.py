
import math

def convert_list(items):
    success = {}
    fail = {}

    for item in items:
        try:
            result = float(item)
        except (ValueError, TypeError) as e:
            fail[item] = f"{type(e).__name__}: {e}"
            continue
        
        if math.isnan(result):
            fail[item] = "Converted but invalid"
            continue

        success[item] = result

    return success, fail


def calculate_success_rate(success, my_list):
    return round((len(success) / len(my_list)) * 100, 2)


def print_messages(result_dict):
    for item, result in result_dict.items():
        print(f"'{item}' --> {result}")


def main():
    items = ['3.5', 'hello', '10', None, '7', 'NaN', '4.2']

    success, fail = convert_list(items)
    success_rate = calculate_success_rate(success, items)

    # Prints:
    print("Successful:")
    print_messages(success)

    print("\nFailed:")
    print_messages(fail)

    print(f"\nSuccess sum: {sum(success.values())}")
    print(f"\nSuccess rate: {success_rate}%\n")


main()