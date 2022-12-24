from tkinter import *
from tkinter import messagebox

class Login:
    #main page
    def __init__(self, root, main):
        self.frame = Frame(root, width=150, height=200, bg="#55423d")
        self.main = main
        self.root = root
        self.root.title("Login")


        #login_page
        self.welcome_text = Label(self.frame, text="Welcome! Please Login", font=('dubai', 13), bg="#55423d", fg="#fffffe")
        self.welcome_text.pack(pady=5)

        #Username
        self.username_text = Label(self.frame, text="Username :", highlightbackground="#e78fb3", fg="#fffffe", font=('dubai', 13, 'bold'), bg='#55423d')
        self.username_text.pack(pady=5)

        #username entry
        self.user_entry = Entry(self.frame, width=25, font=('dubai', 13))
        self.user_entry.pack(pady=5)

        #Password
        self.password_text = Label(self.frame, text="Password :", bg="#55423d", font=('dubai', 13, 'bold'), fg='#fffffe')
        self.password_text.pack(pady=5)
        
        #pasword entry
        self.pass_entry = Entry(self.frame, show='*', width=25, font=('dubai', 13))
        self.pass_entry.pack(pady=5)
        
        #Login_verfy_button
        self.login_button = Button(self.frame, text="Login",fg="#271c19", bg="#ffc0ad", font=('dubai', 13, 'bold'), width=25,command=self.login_verfy, activebackground="#ffc0ad", activeforeground="#271c19")
        self.login_button.pack(pady=5)


    def login_verfy(self):
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "admin":
            messagebox.showinfo("Login", "You have logged in successfully")
            self.frame.pack_forget()
            self.main.frame.pack()
            self.root.title("Library System")
            
        else:
            messagebox.showerror("Error", "Login failed")
            
