
list_a = ["Python", "Java", "C++", "JS"]
list_b = ["Backend", "Mobile", "Systems", "Web"]

def normal_iterate(list_a, list_b):
    for index in range(len(list_a)):
        print(list_a[index] + " " + list_b[index])


def offset_iterate(list_a, list_b):
    shifted_b = list_b[1:] + list_b[:1]
    for index in range(len(list_a)):
        print(list_a[index] + " " + shifted_b[index])


def main():
    print("Normal iteration:")
    normal_iterate(list_a, list_b)
    print("\nReverse iteration:")
    offset_iterate(list_a, list_b)


main()