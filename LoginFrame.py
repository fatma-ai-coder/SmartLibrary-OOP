from tkinter import *
from tkinter import messagebox

class Login:
    #main page
    def __init__(self, root, main):
        self.frame = Frame(root, width=150, height=200, bg='#55423d')
        self.main = main
        self.root = root
        self.root.title("Login")


        #login_page
        self.welcome_text = Label(self.frame, text="Welcome! Please Login", font='Dubai 18 bold', fg='#fffffe', bg='#55423d')
        self.welcome_text.pack(pady=5)

        #Username
        self.username_text = Label(self.frame, text="Username :", font='Dubai', fg='#fff3ec', bg='#55423d')
        self.username_text.pack(pady=5)

        #username entry
        self.user_entry = Entry(self.frame, width=25, bg='white', font='Dubai')
        self.user_entry.pack(pady=5)

        #Password
        self.password_text = Label(self.frame, text="Password :", font='Dubai', fg='#fff3ec', bg='#55423d')
        self.password_text.pack(pady=5)
        
        #pasword entry
        self.pass_entry = Entry(self.frame, show='*', width=25, font='Dubai')
        self.pass_entry.pack(pady=5)
        
        #Login_verfy_button
        self.login_button = Button(self.frame, text="Login", font='Dubai', fg='#271c19', bg='#ffc0ad', activebackground="#ffc0ad",
                                      activeforeground="#271c19", command=self.login_verfy)
        self.login_button.pack(pady=5)


    def login_verfy(self):
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "admin":
            messagebox.showinfo("Login", "You have logged in successfully")
            self.frame.pack_forget()
            self.main.frame.pack()
            self.root.title("Library System")
            
        else:
            messagebox.showerror("Error", "Login failed")
            
