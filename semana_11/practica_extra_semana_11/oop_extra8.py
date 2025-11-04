
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year}."
    
    def __repr__(self):     # for inspections or printing lists of objects.
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year!r})"
    

book1 = Book("Moby-Dick", "Herman Melville", 1851)
book2 = Book("Mapocho", "Nona Fernández", 2002)
book3 = Book("Dune", "Frank Herbert", 1965)

print(book1)

book_list = [book1, book2, book3]
print(book_list)