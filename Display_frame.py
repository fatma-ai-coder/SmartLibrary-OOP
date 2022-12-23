from tkinter import *

 #Display Frame
        self.frame_display = Frame(self.window, width=700, height=500, bg='lightblue')
        display_text = Label(self.frame_display, text="Here the Books we have!!", font=('Poppins 12'))
        display_text.pack(pady=5)
        sort_text = Label(self.frame_display, text="%-20s%-15s%-10s%-5s" % ('Title', 'Author', 'ISBN', "Q"), bg='white',fg='black')
        sort_text.pack(pady=5)
        dis_but = Button(self.frame_display, text="Enter")
        dis_but.place(x=5, y=60)
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