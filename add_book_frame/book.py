from add_book_frame.library_item import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, genre, isbn, authors):
        self.__isbn = isbn
        self.__authors = authors
        super().__init__(title, genre)

    def get_isbn(self):
        return self.__isbn

    def get_authors(self):
        return self.__authors

    def set_authors(self, authors):
        self.__authors = authors

    def __str__(self):
        return super().__str__() + '\nISBN: ' + str(self.__isbn) + '\nAuthors: ' + str(self.__authors)

    def add_to_database(self):
        data = [self.get_title(), self.get_genre(), self.get_stock(), self.__isbn, self.__authors]
        return data