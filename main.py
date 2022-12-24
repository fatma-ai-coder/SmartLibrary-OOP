from tkinter import *
from LoginFrame import Login
from MainMenu import MainMenu


def main():

    # the main window
    root = Tk()

    # Window width and height
    window_width = 600
    window_height = 600

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the coordinates of the main window
    x = (screen_width/2) - (window_width/2)
    y = (screen_height/2) - (window_height/2)

    # Display the window in the middle of the screen
    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    
    root.config(bg="#55423d")
    
    # Instantiate the main menu frame
    main_frame = MainMenu(root)
    
    # Instantiate the Login frame
    login_frame = Login(root, main_frame)
    login_frame.frame.pack()

    root.mainloop()



main()
