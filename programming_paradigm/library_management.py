class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout(self):
        if not self._is_checked_out:
            self.is_checkout_out = True
            return True
        return False

class Library:
    '''Library class to management book checkouts'''
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def checkout_out_book(self,title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"The book '{title}' has been checked out.")
            return !self
        

    def return_book(self,title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"The book '{title}' has been returned.")
                return
        print(f"The book '{title}' is not currently checked out")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

