class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        return f'"{book_name}" added to the library'

    def show_books(self):
        if self.books:
            return f"Books in {self.name}: {self.books}"
        else:
            return "No books available in the library"

# Example usage
lib = Library("City Library")

print(lib.add_book("Python Basics"))
print(lib.add_book("Data Science"))
print(lib.show_books())