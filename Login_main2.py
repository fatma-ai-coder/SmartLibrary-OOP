from tkinter import *

class Login:
    #main page
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x500")
        self.root.title("Login to the Library")
        self.root.configure(bg='lightgreen')
        Login_1 = Button(self.root, text="Login", fg="black", font=('arial', 13, 'bold'), command=self.login_interface)
        Login_1.pack()


    #login_page
    def login_interface(self):
        login_root = Toplevel(self.root)
        login_root.title("Login Page")
        login_root.geometry("700x500")
        login_root.configure(bg='lightgreen')

        text1 = Label(login_root, text="Welcome! Please Login", font=('arial', 13))
        text1.pack()
        text1.place(x=300, y=5)

        #Username
        Username_text = Label(login_root, text="Username :", fg="black", font=('arial', 13, 'bold'))
        Username_text.pack()
        Username_text.place(x=250,y=30)
        self.user_entry = Entry(login_root)
        self.user_entry.pack()
        self.user_entry.place(x=330,y=30)

        #Password
        Password_text = Label(login_root, text="Password :", fg="black", font=('arial', 13, 'bold'))
        Password_text.pack()
        Password_text.place(x=250, y=60)
        self.pass_entry = Entry(login_root)
        self.pass_entry.pack()
        self.pass_entry.place(x=330, y=55)
        #Login_verfy_button
        Login_Button = Button(login_root, text="Login",fg="black", font=('arial', 13, 'bold'),command=self.login_verfy)
        Login_Button.pack()
        Login_Button.place(x=315,y=450)


    def login_verfy(self):
        if self.user_entry.get() == "Rahaf858" and self.pass_entry.get() == "12345rgH":
            s_root = Toplevel()
            s_root.title("Welcome")
            s_root.geometry("700x200")
            s_root.configure(bg='lightgreen')
            s_text = Label(s_root, text="You have log in Successfully", bg="green", width="500", height="5",
                          font=("Calibri", 13, "bold"))
            s_text.pack()

        else:
            f_root = Toplevel()
            f_root.title("Error")
            f_root.geometry("700x200")
            f_root.configure(bg='red')
            f_text = Label(f_root, text="You have wrote the wrong Username or Password", bg="red", width="500", height="1",
                          font=("Calibri", 13))
            f_text.pack()


root = Tk()
object = Login(root)
root.mainloop()