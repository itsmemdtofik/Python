class Book:
    def __str__(self):
        return "This is a Book"


print(str(Book()))  # This is a Book
print(Book())  # This is a Book


class Book:
    def __repr__(self):
        return "Book()"


print(repr(Book()))  # Book()
Book()  # Book()  ← in REPL or console


class Book:
    def __str__(self):
        return "User-Friendly Book"

    def __repr__(self):
        return "Book('Technical representation')"


book = Book()

print(str(book))  # User-Friendly Book
print(repr(book))  # Book('Technical representation')
print(book)  # User-Friendly Book
