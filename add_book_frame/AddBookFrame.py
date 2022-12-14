from tkinter import *
from tkinter import messagebox
from add_book_frame.book import Book


class AddBook:

    # This starts once the class is called
    def __init__(self, window):
        # Frame details
        self.add_book = Frame(window, width=400, height=400)

        # Entry boxes in variables
        self.title = Entry(self.add_book, width=30)
        self.genre = Entry(self.add_book, width=30)
        self.isbn = Entry(self.add_book, width=30)
        self.author1 = Entry(self.add_book, width=30)
        self.author2 = Entry(self.add_book, width=30)
        self.author3 = Entry(self.add_book, width=30)
        self.author4 = Entry(self.add_book, width=30)

        # Labels above the entry boxes
        self.title_label = Label(self.add_book, text='Title:')
        self.genre_label = Label(self.add_book, text='Genre:')
        self.isbn_label = Label(self.add_book, text='ISBN:')
        self.authors_label = Label(self.add_book, text='Author(s): (max. 4)')

        # Packing the widgets in order of appearance
        self.title_label.pack()
        self.title.pack()
        self.genre_label.pack()
        self.genre.pack()
        self.isbn_label.pack()
        self.isbn.pack()
        self.authors_label.pack()
        self.author1.pack()
        self.author2.pack()
        self.author3.pack()
        self.author4.pack()

        # Buttons to submit, exit, and go back
        self.submit_button = Button(self.add_book, text='Submit', command=self.submit_action)
        self.back_button = Button(self.add_book, text='Back', command='')  # hide add_book frame and show main frame
        self.submit_button.pack()
        self.back_button.pack()

        # Pack the frame to the main window
        self.add_book.pack()


    # The command when the "Submit" button is pressed
    def submit_action(self):

        # Iterate over the authors and add the non-empty variables to a list
        authors_list = [self.author1.get(), self.author2.get(), self.author3.get(), self.author4.get()]
        temp = authors_list.copy()
        for i in authors_list:
            if i == "":
                temp.remove(i)
        authors_list = temp

        # Check if the ISBN has a valid input
        u_isbn = self.isbn.get()
        try:
            u_isbn = int(u_isbn)
        except ValueError:
            messagebox.showerror('Error', "Invalid ISBN, must be numerical value.")
            return

        # Create a book object
        new_book = Book(self.title.get(), self.genre.get(), u_isbn, authors_list)

        # Write the book details in the text file
        books_database = open('books.txt', 'a')
        books_database.write('\n')
        var = new_book.add_to_database()
        books_database.write(str(var))
        books_database.close()

        # Popup to confirm addition of the book to the database
        messagebox.showinfo('Add Book', 'New book added successfully!')

        # Clear the entry boxes
        self.title.delete(0, END)
        self.genre.delete(0, END)
        self.isbn.delete(0, END)
        self.author1.delete(0, END)
        self.author2.delete(0, END)
        self.author3.delete(0, END)
        self.author4.delete(0, END)

