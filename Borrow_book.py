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
                
        self.heading_window = Label(self.frame, text="Borrow Books from the Library", font=("dubai", 10), bg="#55423d", fg="#fffffe")
        self.heading_window.pack(pady=5)

        self.id = Label(self.frame, text='Borrower ID', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.id2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.id.pack()
        self.id2.pack()

        self.borrow_name =Label(self.frame, text='The Borrower Name', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.borrow_name2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.borrow_name.pack()
        self.borrow_name2.pack()

        self.book_name = Label(self.frame, text='Book Name', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.book_name2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.book_name.pack()
        self.book_name2.pack()

        self.isbn = Label(self.frame, text='ISBN ', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.isbn2 = Entry(self.frame, width=25, font=("dubai", 10))
        self.isbn.pack()
        self.isbn2.pack()

        

        def get_date():
            self.return_date.config(text= "Return date should be on" + self.cal.get_date(), font=("dubai", 10))
            
        self.cal = Calendar(self.frame, selectmode="day", year=2022, month=12, day=15 )
        self.cal.pack() 
        

        self.return_date2 = Button(self.frame, text="Return Data", command=get_date, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.return_date2.pack()

        self.return_date = Label(self.frame, text='Return Date ', bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.return_date.pack(pady=10)

        self.borrow = Button(self.frame, text= 'Borrow',width=25, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.borrow.pack()

        self.back_button = Button(self.frame, text="Back", command=self.change_frame, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.back_button.pack(pady=5)
        
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        self.root.title("Library System")
