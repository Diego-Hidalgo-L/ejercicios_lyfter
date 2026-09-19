
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    print_user_info(name="Diego", age=30, country="Costa Rica")


main()