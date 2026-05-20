

def input_category_info(categories):
    category = input("Enter the name of the category: ")
    color = input("Enter the color for the category: ")

    new_category = {}

    new_category["category"] = category
    new_category["color"] = color

    categories.append(new_category)


def main():
    categories = []

    input_category_info(categories)
    print(categories)


main()