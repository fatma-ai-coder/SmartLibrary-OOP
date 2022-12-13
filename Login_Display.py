from tkinter import *
from tkinter import messagebox


class LMS:
    def __init__(self):
        self.window = Tk()
        self.Books = "Books.txt"
        window_width = 310
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.window.title("Library System Management")

        #-------------------Login Frame--------------------
        self.frame_login = Frame(self.window, width=310, height=300, bg='lightblue')

        self.heading = Label(self.frame_login, text="LOGIN", font=('arial', 13, 'bold'))
        self.heading.pack(pady=5)
        #Username
        self.username = Label(self.frame_login, text="username *", height=1, bg="white", fg="black",font=('arial', 13, 'bold'))
        self.username.pack(pady=5)

        self.e_name = Entry(self.frame_login, width=25, font=("", 15))
        self.e_name.pack(pady=5)
        #Password
        self.password = Label(self.frame_login, text="password *", height=1, bg="white", fg="black",font=('arial', 13, 'bold'))
        self.password.pack(pady=5)

        self.e_password = Entry(self.frame_login, width=25, show='*', font=("", 15), highlightthickness=1)
        self.e_password.pack(pady=5)

        self.button_confirm = Button(self.frame_login, text="Login", width=39, height=2, font=("Ivy 9 bold"), command=self.check_password)
        self.button_confirm.pack(pady=5)
        self.frame_login.pack()

        #main Frame
        self.frame_main = Frame(self.window, width=310, height=300, bg="lightblue")
        welcome_msg = Label(self.frame_main, text="Welcome to our Library",height=3, font=('arial', 13, 'bold'))
        welcome_msg.pack(pady=5)
        #-----------------add_button----------------------
        but_add = Button(self.frame_main, text='Add', font=("Ivy 9 bold"))
        but_add.pack(pady=5)

        #---------------borrow button----------------------
        but_borrow = Button(self.frame_main, text='Borrow',  font=("Ivy 9 bold"))
        but_borrow.pack(pady=5)

        #---------------return_button---------------------
        but_return = Button(self.frame_main, text='Return',  font=("Ivy 9 bold"))
        but_return.pack(pady=5)

        #----------------display button-------------------
        but_display_bal = Button(self.frame_main, text='Display',font=("Ivy 9 bold"), command=self.Display_Books)
        but_display_bal.pack(pady=5)

        #-----------------Exit_button---------------------
        ExitButton = Button(self.frame_main, text="Exit", command=self.ExitPush)
        ExitButton.pack()




        #Display Frame
        self.frame_display = Frame(self.window, width=700, height=500, bg='lightblue')
        display_text = Label(self.frame_display, text="Here the Books we have!!", font=('Poppins 12'))
        display_text.pack(pady=5)
        sort_text = Label(self.frame_display, text="%-20s%-15s%-10s%-5s" % ('Title', 'Author', 'ISBN', "Q"), bg='white',fg='black')
        sort_text.pack(pady=5)
        Books = open("Books.txt", "r")
        viewBokks = Books.read()
        text2 = Label(self.frame_display, text=viewBokks)
        text2.place(x=2, y=60)
        ExitButton = Button(self.frame_display, text="Exit", command=self.ExitPush)
        ExitButton.pack(pady=90)

        self.window.mainloop()








#functions (command)

    def Display_Books(self):
        self.frame_display.pack()
        self.frame_main.pack_forget()

    def ExitPush(self):
        self.frame_main.quit()


    def check_password(self):
        name = self.e_name.get()
        password = str(self.e_password.get())

        if name == 'admin' and password == 'admin':
            messagebox.showinfo('Login', 'Welcome to the Library')
            self.frame_login.pack_forget()
            self.frame_main.pack()
        else:
            messagebox.showinfo('Login Failed')

#-----------object-----------------
obj = LMS()