from tkinter import *
from tkinter import messagebox


class Login_Interface:
    def __init__(self):
        self.balance = 100
        self.window = Tk()

        window_width = 310
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.window.title("Login")

        self.frame_login = Frame(self.window, width=150, height=200,
                                 bg='lightblue')
        # frame_login widgets

        self.heading = Label(self.frame_login, text="LOGIN", font=('Poppins 23'))
        self.heading.pack(pady=5)

        self.username = Label(self.frame_login, text="username *", height=1, bg="white", fg="black",
                              font=('Poppins 12'))
        self.username.pack(pady=5)

        self.e_name = Entry(self.frame_login, width=25, font=("", 15))
        self.e_name.pack(pady=5)

        self.password = Label(self.frame_login, text="password *", height=1, bg="white", fg="black",
                              font=('Poppins 12'))
        self.password.pack(pady=5)

        self.e_password = Entry(self.frame_login, width=25, show='*', font=("", 15), highlightthickness=1)
        self.e_password.pack(pady=5)

        self.button_confirm = Button(self.frame_login, text="Login", width=39, height=2, font=("Ivy 9 bold"),
                                     command=self.check_password)
        self.button_confirm.pack(pady=5)
        self.frame_login.pack()

        #main interface
        self.frame_main = Frame(self.window, width=310, height=400)
        welcome_msg = Label(self.frame_main, text="Welcome to our Library",
                            height=3, font=('Poppins 12'))
        welcome_msg.pack(pady=5)
        but_add = Button(self.frame_main, text='Add', font=("Ivy 9 bold"))
        but_add.pack(pady=5)
        but_borrow = Button(self.frame_main, text='Borrow',  font=("Ivy 9 bold"))
        but_borrow.pack(pady=5)
        but_display_bal = Button(self.frame_main, text='Display',font=("Ivy 9 bold"))
        but_display_bal.pack(pady=5)

        self.window.mainloop()

    def check_password(self):
        name = self.e_name.get()
        password = str(self.e_password.get())

        if name == 'admin' and password == 'admin':
            messagebox.showinfo('Login', 'Welcome to the Library')
            self.frame_login.pack_forget()
            self.frame_main.pack()
        else:
            messagebox.showinfo('Login Failed')

obj = Login_Interface()