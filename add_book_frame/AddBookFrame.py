from tkinter import *
from tkinter import messagebox
from add_book_frame.BookClass import Book
import json


class AddBook:

    # This starts once the class is called
    def __init__(self, window, main):
        # Frame details
        self.frame = Frame(window, width=400, height=400)
        self.main = main
        self.root = window

        # Change the title to Add Book
        self.root.title("Add book")

        # Entry boxes in variables
        self.title = Entry(self.frame, width=30)
        self.genre = Entry(self.frame, width=30)
        self.isbn = Entry(self.frame, width=30)
        self.author1 = Entry(self.frame, width=30)
        self.author2 = Entry(self.frame, width=30)
        self.author3 = Entry(self.frame, width=30)
        self.author4 = Entry(self.frame, width=30)
        self.stock = Entry(self.frame, width=30)

        # Notice that all fields are mandatory
        self.notice = Label(self.frame, text='Please note that all fields are mandatory.')

        # Labels above the entry boxes
        self.title_label = Label(self.frame, text='Title:')
        self.genre_label = Label(self.frame, text='Genre:')
        self.isbn_label = Label(self.frame, text='ISBN:')
        self.authors_label = Label(self.frame, text='Author(s): (max. 4)')
        self.stock_label = Label(self.frame, text='Stock')

        # Empty labels to create a space between the entries and buttons for better appearance
        self.spacer = Label(self.frame)

        # Set the menu initially
        self.menu = StringVar()
        self.menu.set("Select Genre ...")
        # Create a dropdown menu
        self.genre_drop = OptionMenu(self.frame, self.menu, "Fantasy", "Science Fiction", "Horror", "Mystery", "Romance", "Nonfiction")

        # Packing the widgets in order of appearance
        self.notice.pack(pady=15)
        self.title_label.pack()
        self.title.pack()
        self.genre_label.pack()
        self.genre_drop.pack()
        self.isbn_label.pack()
        self.isbn.pack()
        self.authors_label.pack()
        self.author1.pack()
        self.author2.pack()
        self.author3.pack()
        self.author4.pack()
        self.stock_label.pack()
        self.stock.pack()
        self.spacer.pack()

        # Buttons to submit and go back
        self.submit_button = Button(self.frame, text='Submit', command=self.submit_action)
        self.back_button = Button(self.frame, text='Back', command=self.change_frame)  # hide add_book frame and show main frame
        self.submit_button.pack()
        self.back_button.pack()

    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        self.root.title("Library System")



    # The command when the "Submit" button is pressed
    def submit_action(self):

        # Check that all fields are filled and nothing is empty
        for x in (self.title.get(), self.menu.get(), self.isbn.get(), self.author1.get(), self.stock.get()):
            if x == '' or self.menu.get() == "Select Genre ...":
                messagebox.showerror('Error', 'Please fill all required fields.')
                return

        # Iterate over the authors and add the non-empty variables to a list
        authors_list = [self.author1.get(), self.author2.get(), self.author3.get(), self.author4.get()]
        temp = authors_list.copy()
        for i in authors_list:
            if i == "":
                temp.remove(i)
        authors_list = temp

        # Check if the ISBN entered by the user has a valid input
        u_isbn = self.isbn.get()
        try:
            u_isbn = int(u_isbn)
            # store the number of digits in the isbn in digits
            digits = len(str(u_isbn))
            # check if the number of digits is either 10 or 13
            if digits != 10 and digits != 13:
                messagebox.showerror("Error", "Invalid ISBN, must be 10 or 13 digits.")
                return
        except ValueError:
            messagebox.showerror('Error', "Invalid ISBN, must be numerical value.")
            return

        # Check if the stock entered by the user has a valid input
        u_stock = self.stock.get()
        try:
            u_stock = int(u_stock)
            # check if the stock is less than 0
            if u_stock < 0:
                messagebox.showerror('Error', "Invalid stock, must be greater than 0")
        except ValueError:
            messagebox.showerror('Error', "Invalid stock, must be numerical value.")
            return

        # Create a book object
        new_book = Book(self.title.get(), self.menu.get(), u_isbn, authors_list, u_stock)

        # Write the book details in the text file
        books_database = open('books.txt', 'a')
        books_database.write('\n')
        var = new_book.add_to_database()
        books_database.write(json.dumps(var))
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
        self.stock.delete(0, END)
