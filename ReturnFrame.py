from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import json


class ReturnBook:
    '''This class represents the return_book frame in the library system.'''
    
    def __init__(self, root, main):
        self.frame = Frame(root, width=300, height=310)
        self.frame.pack(pady=5)
        self.main = main
        
        # borrower name label
        self.u_name = Label(self.frame, text="Name*:")
        self.u_name.pack(pady=5)
        
        # borrower name entry
        self.name_entry = Entry(self.frame, width=25)
        self.name_entry.pack(pady=5)
        
        # user id widgets
        # User ID label
        self.u_id = Label(self.frame, text="ID Number*:")
        self.u_id.pack(pady=5)
        
        # ID entry box
        self.id_entry = Entry(self.frame, width=25)
        self.id_entry.pack(pady=5)
        
        # Book name
        self.b_name = Label(self.frame, text="Book Name*:")
        self.b_name.pack(pady=5)
        
        self.book_name_entry = Entry(self.frame, width=25)
        self.book_name_entry.pack(pady=5)
        
        # The Book's isbn widgets
        # isbn label
        self.isbn = Label(self.frame, text="ISBN Number*:")
        self.isbn.pack(pady=5)
        
        # isbn entry box
        self.isbn_entry = Entry(self.frame, width=25)
        self.isbn_entry.pack(pady=5)
        
        # Borrowed date label
        self.borrow_date = Label(self.frame, text="Date borrowed*:")
        self.borrow_date.pack(pady=5)
        
        # Borrowed date calendar
        self.calendar = Calendar(self.frame, selectmode="day")
        self.calendar.pack(pady=5)
        
        #the submission widget
        # the submit button
        self.submit_button = Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.pack(pady=5)
                  
        # the back button                
        self.back_button = Button(self.frame, text='Back', command=self.change_frame)
        self.back_button.pack()

    # change the frame when the back button is clicked
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        
    # the submission button's functionality
    def submit(self):
        
        #check if all fields have been submitted
        if self.name_entry.get() == "" or self.isbn_entry.get() == "" or self.id_entry.get() == "" or self.book_name_entry.get() == "":
            pass
        print(self.calendar.date)
        #check if isbn is valid
        #check if date is before the current date
        
        # load books.txt to increment the stock
        with open("books.txt", "w+") as file:
            books = file.readlines()
            
            
            for i in range(len(books)):
                books[i] = json.loads(books[i]) 
                
            for book in books:
                if book["isbn"] == int(self.isbn_entry.get()):
                    book["stock"] += 1
            
            file.seek(0)
            print(books)
            for book in books:
                file.write(json.dumps(book))
            
        
        with open("borrowers_returns.txt", "r+") as file:
            borrowed_books = file.readlines()
            file.seek(0)
            
            for i in range(len(borrowed_books)):
                borrowed_books[i] = json.loads(borrowed_books[i])
            
            print("passed borrowers_returns.txt")
                
            for book in borrowed_books:
                if book["isbn"] != int(self.isbn_entry.get()):
                    file.write(json.dumps(book))
            file.truncate()
                    
                    
            messagebox.showinfo("Book returned", "The book was successfully returned.")
            
