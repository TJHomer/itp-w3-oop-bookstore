class Bookstore(object):
    def __init__ (self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books

    def search_books(self, title=None, author=None):
        search_list = []
        for book in self.books:
            if title is not None:
                if title.lower() in book.title.lower():
                    search_list.append(book)
            if author == book.author:
                search_list.append(book)
        return search_list

class Author(object):
    def __init__ (self, name, nationality):
        self.name = name 
        self.nationality = nationality
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.add_book(self)
