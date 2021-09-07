# Example 2

from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        self.lblText = Label(frame, text="This is a label widget")
        self.btnQuit = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.btnHello = Button(frame, text="Hello", command=self.SaySomething)

        frame.grid(column=0, row=0)
        self.lblText.grid(column=0, row=0, columnspan=2)
        self.btnHello.grid(column=0, row=1)
        self.btnQuit.grid(column=1, row=1)

    def SaySomething(self):
        print("Hello to FullCircle Magazine Readers!!!!!!!!!!")

root = Tk()
root.geometry('250x175+50+250')
app = App(root)
root.mainloop()