class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    '''Library class to management book checkouts'''
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def checkout_out_book(title):
        pass

    def return_book(title):
        pass

    def list_available_books(self):
        pass
