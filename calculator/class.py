class Library:

 def _init_(self, name, total_books):
        self.name = name
        self.total_books = total_books

def show_library_name(self):
        return f"{self.name} Library"

def show_total_books(self):
        return f"Total books: {self.total_books}"


# Creating an object of Library class
library1 = Library("City Central", 5000)

# Printing details
print(library1.show_library_name())
print(library1.show_total_books())