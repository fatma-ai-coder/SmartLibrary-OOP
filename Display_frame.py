from tkinter import *
import json
from tkinter import messagebox

#Display Frame
class DisplayBooks:
    def __init__(self, root, main):
        self.root = root
        self.root.title("Display Available Books")
        self.main = main
        self.frame = Frame(self.root, width=600, height=500, bg="#55423d")
        self.frame.pack()
        self.info_frame = Frame(self.frame, width=300, height=300, bg="#55423d")
        
        self.book_number = Label(self.info_frame)
        self.book_title = Label(self.info_frame)
        self.authors = Label(self.info_frame)
        self.isbn = Label(self.info_frame)
        self.stock = Label(self.info_frame)
        self.space = Label(self.info_frame, bg="#55423d")

        display_text = Label(self.frame, text="Here are the books we have!", font=('Dubai', 13), fg="#fffffe", bg="#55423d")
        display_text.pack(pady=5)

        file = open("Books.txt", "r")
        self.books = file.readlines()
        for i in range(len(self.books)):
            self.books[i] = json.loads(self.books[i])
        
        scroll = Scrollbar(self.frame)
        scroll.pack(side="right", fill=Y)
        
        self.test_list = Listbox(self.frame, yscrollcommand=scroll.set, selectmode="single")

        for book in self.books:
            
            self.test_list.insert(END, book["title"])
            
        file.close()
        self.test_list.pack(side="left")
        scroll.config(command=self.test_list.yview)

        dis_but = Button(self.frame, text="Enter", command=self.display_info, font=("dubai", 10), bg="#ffc0ad", fg="#271c19", activebackground="#ffc0ad", activeforeground="#271c19")
        dis_but.pack(pady=5)

        back_button = Button(self.frame, text="Back", command=self.change_frame, bg="#ffc0ad", fg="#271c19", font=("dubai",10), activebackground="#ffc0ad", activeforeground="#271c19")
        back_button.pack(pady=5)

    #functions (command)
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        self.root.title("Library System")
        
    def display_info(self):
        self.info_frame.pack()
        try:
            index = self.test_list.curselection()[0]
        
            self.book_title.config(text="Title: " + str(self.books[index]["title"]), bg="#55423d", fg="#fff3ec", font=("dubai", 10))
            self.book_title.pack(pady=5)
            
            self.authors.config(text="Authors: " + str(self.books[index]["authors"]), bg="#55423d", fg="#fff3ec", font=("dubai", 10))
            self.authors.pack(pady=5)
            
            self.isbn.config(text="ISBN: " + str(self.books[index]["isbn"]), bg="#55423d", fg="#fff3ec", font=("dubai", 10))
            self.isbn.pack(pady=5)
            
            self.stock.config(text="Stock: " + str(self.books[index]["stock"]), bg="#55423d", fg="#fff3ec", font=("dubai", 10))
            self.stock.pack(pady=5)
            
            self.space.pack(pady=5)
        
        except IndexError:
            messagebox.showerror("Error", "Please select a book to see info")