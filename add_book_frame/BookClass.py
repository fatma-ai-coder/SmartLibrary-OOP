class Book:

    def __init__(self, title, genre, isbn, authors, stock):
        # define all instance attributes and set them to private
        self.__title = title
        self.__genre = genre
        self.__isbn = isbn
        self.__authors = authors
        self.__stock = stock

    # methods that act as getters (accessors) for each private attribute
    def get_isbn(self):
        return self.__isbn

    def get_authors(self):
        return self.__authors

    def get_stock(self):
        return self.__stock

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    # method to return the details of the book organized in a list
    def add_to_database(self):
        data = [self.get_title(), self.get_genre(), self.__isbn, self.__authors, self.get_stock()]
        return data