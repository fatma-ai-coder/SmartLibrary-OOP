from tkinter import *
from LoginFrame import Login
from MainMenu import MainMenu


def main():

    root = Tk()

    window_width = 600
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (window_width/2)
    y = (screen_height/2) - (window_height/2)

    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    root.config(bg='#55423d')
    
    main_frame = MainMenu(root)
    login_frame = Login(root, main_frame)
    login_frame.frame.pack()

    root.mainloop()


main()
