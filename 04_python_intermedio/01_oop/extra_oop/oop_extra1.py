
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


book1 = Book("Moby-Dick", "Herman Melville", 1851)
book2 = Book("Mapocho", "Nona Fernández", 2002)
book3 = Book("Dune", "Frank Herbert", 1965)

def main():
    print(f"'{book1.title}' by {book1.author}, published in {book1.year}.")
    print(f"'{book2.title}' by {book2.author}, published in {book2.year}.")
    print(f"'{book3.title}' by {book3.author}, published in {book3.year}.")


main()