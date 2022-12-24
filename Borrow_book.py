from tkinter import *
from tkcalendar import *
from tkinter import messagebox


class BorrowBook:
    def __init__(self, root, main):
        self.frame = Frame(root, width=510, height=500, bg="#55423d")
        self.frame.pack()
        self.root = root
        self.root.title("Borrow Book")
        self.main = main
                
        # The heading of the frame
        self.heading_window = Label(self.frame, text="Borrow Books from the Library", font=("dubai", 10), bg="#55423d", fg="#fffffe")
        self.heading_window.pack(pady=5)

        # user ID Entry
        self.id = Label(self.frame, text='Borrower ID', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.id2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.id.pack()
        self.id2.pack()

        # User name Entry
        self.borrow_name =Label(self.frame, text='The Borrower Name', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.borrow_name2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.borrow_name.pack()
        self.borrow_name2.pack()

        # book name Entry
        self.book_name = Label(self.frame, text='Book Name', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.book_name2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.book_name.pack()
        self.book_name2.pack()

        # ISBN number entry
        self.isbn = Label(self.frame, text='ISBN ', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.isbn2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.isbn.pack()
        self.isbn2.pack()

        
        # this function changes the return date label
        def get_date():
            self.return_date.config(text= "Return date should be on" + self.cal.get_date(), font=("dubai", 10))
            
        # Creating calendar widget
        self.cal = Calendar(self.frame, selectmode="day", year=2022, month=12, day=15 )
        self.cal.pack() 
        
        # The button that displays the date
        self.return_date2 = Button(self.frame, text="Return Data", command=get_date, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.return_date2.pack()

        # The label where the date will be displayed when return_date2 is clicked
        self.return_date = Label(self.frame, text='Return Date ', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.return_date.pack(pady=10)

        # the borrow button
        self.borrow = Button(self.frame, text= 'Borrow',width=25, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19", command=self.borrow_book)
        self.borrow.pack()

        # The back button that changes the frame to the main menu frame
        self.back_button = Button(self.frame, text="Back", command=self.change_frame, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.back_button.pack(pady=5)
        
    # This function changes the frame from the current to the main frame
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        self.root.title("Library System")

    def borrow_book(self):
        # check if any field is empty
        if self.id2.get() == "" or self.borrow_name2.get() == "" or self.book_name2.get() == "" or self.isbn2.get() == "":
            messagebox.showerror("Error", "Please fill all the missing fields")

        else:
            messagebox.showinfo("Book Borrowed", "The book has been borrowed successfully")
