class LibraryItem:

    def __init__(self, title, genre):
        self.__title = title
        self.__genre = genre
        self.__inStock = True

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_stock(self):
        return self.__inStock

    def set_stock(self):
        pass

    def __str__(self):
        t1 = "Title: " + self.__title
        g1 = "Genre: " + self.__genre
        a1 = "Available: " + str(self.__inStock)
        return t1 + '\n' + '\n' + g1 + '\n' + a1
