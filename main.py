from tkinter import *
from tkinter import messagebox
from Login_main2 import Login
from add_book_frame.AddBookFrame import AddBook


def main():
    root = Tk()

    window_width = 310
    window_height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (window_width/2)
    y = (screen_height/2) - (window_height/2)

    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    root.config(bg="white")
    AddBook(root)
    root.title("Login")
    root.mainloop()

main()
