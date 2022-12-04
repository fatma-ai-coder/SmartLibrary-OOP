from tkinter import *
from tkinter import ttk

SIZE = 200

root = Tk()

frame = ttk.Frame(root, padding = SIZE)
frame.grid()
ttk.Label(frame, text = "hello world").grid(column = 0, row = 1)

ttk.Button(frame, text = "Quit", command= root.destroy).grid(column = 0, row =3)
ttk.Label(frame, text = "hello", anchor= "center", background= "navy", font= "Helvetica", foreground= "pink").grid(column = 3, row = 1)
ttk.Scrollbar(frame, orient= "horizontal", takefocus= 100).grid(column =7, row= 9)

root.mainloop()
