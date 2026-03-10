
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"'{self.title}' de {self.author}"
    
    def __repr__(self):
        return f"{self.title!r}-{self.author!r}-{self.year!r}"


class Library:
    def __init__(self, max_books):
        self.max_books = max_books
        self.books = []

    def add_book(self, book):
        if len(self.books) >= self.max_books:
            return "La biblioteca está llena."

        self.books.append(book)

    def remove_book(self, book):
        if not self.books:
            return "No hay libros para remover."
        if book not in self.books:
            return f"El libro {book} no se encuentra en la biblioteca."
        
        self.books.remove(book)
        return f"Se ha removido el libro: {book}"


def main():
    book1 = Book("Moby-Dick", "Herman Melville", 1851)
    book2 = Book("Mapocho", "Nona Fernández", 2002)
    book3 = Book("Dune", "Frank Herbert", 1965)
    book4 = Book("For Whom the Bell Tolls", "Ernest Hemingway", 1940)
    book5 = Book("Temporada de Huracanes", "Fernanda Melchor", 2017)

    my_books = [book1, book2, book3]
    my_library = Library(4, my_books)

    print(my_books)
    my_library.add_book(book4)
    print(my_books)
    print(my_library.remove_book(book5))
    print(my_books)


main()