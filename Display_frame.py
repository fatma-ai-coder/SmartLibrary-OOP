from tkinter import *
import json

 #Display Frame
class DisplayBooks:
    def __init__(self, root, main):
        self.root = root
        self.root.title("Display Available Books")
        self.main = main
        self.frame = Frame(self.root, width=500, height=500)
        self.frame.pack()

        display_text = Label(self.frame, text="Here are the Books we have!!", font=('Poppins 12'))
        display_text.pack(pady=5)

        #sort_text = Label(self.frame, text="%-20s%-15s%-10s%-5s" % ('Title', 'Author', 'ISBN', "Q"), bg='white',fg='black')
        #sort_text.pack(pady=5)

        file = open("Books.txt", "r")
        books = file.readlines()
        for i in range(len(books)):
            books[i] = json.loads(books[i])

        count = 0
        for book in books:
            count += 1
            Label(self.frame, text="Book: " + str(count)).pack(pady=5)
            Label(self.frame, text="Title: " + str(book["title"])).pack(pady=5)
            Label(self.frame, text="Authors: " + str(book["authors"])).pack(pady=5)
            Label(self.frame, text="ISBN: " + str(book["isbn"])).pack(pady=5)
            Label(self.frame, text="Stock: " + str(book["stock"])).pack(pady=5)
            Label(self.frame).pack(pady=5)


        dis_but = Button(self.frame, text="Enter")
        dis_but.pack(pady=5)

        back_button = Button(self.frame, text="Back", command=self.change_frame)
        back_button.pack(pady=5)

     #functions (command)
    def change_frame(self):
        self.frame.pack_forget()
        self.main.pack()
        self.root.title("Library System")