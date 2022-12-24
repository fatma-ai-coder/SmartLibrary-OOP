from tkinter import *
from tkinter import messagebox
from add_book_frame.AddBookFrame import AddBook
from ReturnFrame import ReturnBook
from Borrow_book import BorrowBook
from Display_frame import DisplayBooks


class MainMenu:
    
    def __init__(self, root):
        self.frame = Frame(root, width=300, height=400, bg="#55423d")
        self.root = root
        self.root.title("Library System")

        self.add_book_button = Button(self.frame, text="Add Book", width=35, pady=10, command=self.change_add_book,
                                      bg="#ffc0ad", fg="#271c19", font=("dubai",10), activebackground="#ffc0ad", activeforeground="#271c19")
        self.add_book_button.pack(ipadx=20, ipady=5, pady=10)
        
        self.borrow_book_button = Button(self.frame, text="Borrow Book", width=35, pady=10, command=self.change_borrow,
                                         bg="#ffc0ad", fg="#271c19", font=("dubai",10), activebackground="#ffc0ad", activeforeground="#271c19")
        self.borrow_book_button.pack(ipadx=20, ipady=5, pady=10)
        
        self.return_button = Button(self.frame, text="Return Book", width=35, pady=10, command=self.change_return,
                                    bg="#ffc0ad", fg="#271c19", font=("dubai",10), activebackground="#ffc0ad", activeforeground="#271c19")
        self.return_button.pack(ipadx=20, ipady=5, pady=10)
        
        self.display_button = Button(self.frame, text="Display Book", command=self.change_display, width=35, pady=10,
                                     bg="#ffc0ad", fg="#271c19", font=("dubai",10), activebackground="#ffc0ad", activeforeground="#271c19")
        self.display_button.pack(ipadx=20, ipady=5, pady=10)
        
        self.exit_button = Button(self.frame, text="Exit", command=self.exit_funct, width=35, pady=10, bg="#ffc0ad",
                                  fg="#271c19", font=("dubai",10), activebackground="#ffc0ad", activeforeground="#271c19")
        self.exit_button.pack(ipadx=20, ipady=5, pady=10)
        
        
        
        
    def exit_funct(self):
        leave = messagebox.askyesno("Exit", "Do you want to exit?")
        if leave == True:
            exit()
        else:
            pass
        
    def change_add_book(self):
        self.frame.pack_forget()
        AddBook(self.root, self.frame).frame.pack()
        
    def change_borrow(self):
        self.frame.pack_forget()
        BorrowBook(self.root, self.frame).frame.pack()
    
    def change_return(self):
        self.frame.pack_forget()
        ReturnBook(self.root, self.frame).frame.pack()
    
    def change_display(self):
        self.frame.pack_forget()
        DisplayBooks(self.root, self.frame).frame.pack()
