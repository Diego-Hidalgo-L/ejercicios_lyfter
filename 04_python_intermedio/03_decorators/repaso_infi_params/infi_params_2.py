
def print_arguments(*args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")


def main():
    print_arguments("apple", "banana", "cherry")


main()