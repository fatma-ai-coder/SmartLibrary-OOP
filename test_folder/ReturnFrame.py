from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar



class ReturnBook:
    '''This class represents the return_book frame in the library system.'''
    
    def __init__(self, root, main):
        self.frame = Frame(root, width=300, height=310, bg="#55423d")
        self.frame.pack(pady=5)
        self.main = main
        self.root = root
        self.root.title("Return Book")
        
        # borrower name label
        self.u_name = Label(self.frame, text="Name*:", bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.u_name.pack(pady=3)
        
        # borrower name entry
        self.name_entry = Entry(self.frame, width=25, font=("dubai", 10))
        self.name_entry.pack(pady=3)
        
        # user id widgets
        # User ID label
        self.u_id = Label(self.frame, text="ID Number*:", bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.u_id.pack(pady=3)
        
        # ID entry box
        self.id_entry = Entry(self.frame, width=25, font=("dubai", 10))
        self.id_entry.pack(pady=3)
        
        # Book name
        self.b_name = Label(self.frame, text="Book Name*:", bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.b_name.pack(pady=3)
        
        self.book_name_entry = Entry(self.frame, width=25, font=("dubai", 10))
        self.book_name_entry.pack(pady=3)
        
        # The Book's isbn widgets
        # isbn label
        self.isbn = Label(self.frame, text="ISBN Number*:", bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.isbn.pack(pady=3)
        
        # isbn entry box
        self.isbn_entry = Entry(self.frame, width=25, font=("dubai", 10))
        self.isbn_entry.pack(pady=3)
        
        # Borrowed date label
        self.borrow_date = Label(self.frame, text="Date borrowed*:", bg="#55423d", fg="#fff3ec", font=("dubai", 10))
        self.borrow_date.pack(pady=3)
        
        # Borrowed date calendar
        self.calendar = Calendar(self.frame, selectmode="day")
        self.calendar.pack(pady=3)
        
        #the submission widget
        # the submit button
        self.submit_button = Button(self.frame, text="Submit", command=self.submit, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.submit_button.pack(pady=3)
                  
        # the back button                
        self.back_button = Button(self.frame, text='Back', command=self.change_frame, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        self.back_button.pack()

    # change the frame when the back button is clicked
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        
    # the submission button's functionality
    def submit(self):
        
        #check if all fields have been submitted
        if self.name_entry.get() == "" or self.isbn_entry.get() == "" or self.id_entry.get() == "" or self.book_name_entry.get() == "":
            messagebox.showerror("Error", "Missing fields")
            return
        messagebox.showinfo("Book returned", "The book was successfully returned.")
            
