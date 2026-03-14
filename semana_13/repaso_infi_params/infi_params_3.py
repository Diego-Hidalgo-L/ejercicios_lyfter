
def greet_people(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")


def main():
    greet_people("Hello", "Ana", "Luis", "Pedro")


main()