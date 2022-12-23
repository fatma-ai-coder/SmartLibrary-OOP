from tkinter import *
from tkcalendar import *
from tkinter import messagebox


class BorrowBook:
    def __init__(self, root, main):
        self.frame = Frame(root, width=510, height=500, bg="white")
        self.frame.pack()
        self.root = root
        self.root.title("Borrow Book")
        self.main = main
                
        self.heading_window = Label(self.frame, text="Borrow Books from the Library", font=('arial', 13, 'bold'))
        self.heading_window.pack(pady=5)

        self.id = Label(self.frame, text='Borrower ID',  font=("Ivy 9 bold"))
        self.id2 = Entry(self.frame, width=25, font=("", 15))
        self.id.pack()
        self.id2.pack()

        self.borrow_name =Label(self.frame, text='The Borrower Name',  font=("Ivy 9 bold"))
        self.borrow_name2 = Entry(self.frame, width=25, font=("", 15))
        self.borrow_name.pack()
        self.borrow_name2.pack()

        self.book_name = Label(self.frame, text='Book Name',  font=("Ivy 9 bold"))
        self.book_name2 = Entry(self.frame, width=25, font=("", 15))
        self.book_name.pack()
        self.book_name2.pack()

        self.isbn = Label(self.frame, text='ISBN ',  font=("Ivy 9 bold"))
        self.isbn2 = Entry(self.frame, width=25, font=("", 15))
        self.isbn.pack()
        self.isbn2.pack()

        

        def grab_date():
            self.return_date.config(text= "Return date should be on" + self.cal.get_date())
            
        self.cal = Calendar(self.frame, selectmode="day", year=2022, month=12, day=15 )
        self.cal.pack() 
        

        self.return_date2 = Button(self.frame, text="Return Data", command= grab_date)
        self.return_date2.pack()

        self.return_date = Label(self.frame, text='Return Date ',  font=("Ivy 9 bold"))
        self.return_date.pack(pady=10)

        self.borrow = Label(self.frame, text=' Borrow ',  font=("Ivy 9 bold"))
        self.borrow2 = Button(self.frame, text= 'Borrow',width=25, font=("", 15))
        self.borrow.pack()
        self.borrow2.pack()

        self.back_button = Button(self.frame, text="Back", command=self.change_frame)
        self.back_button.pack(pady=5)
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        self.root.title("Library System")
