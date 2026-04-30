from tkinter import *
class Test:
    def __init__(self):
        top = Tk()
        L1 = Label(top, text="Physics")
        L1.place(x=10, y=10)
        E1 = Entry(top, bd=5).place(x=60, y=10)
        L2 = Label(top, text="Maths").place(x=10, y=50)
        E2 = Entry(top, bd=5).place(x=60, y=50)
        L3 = Label(top, text="Total").place(x=10, y=150)
        E3 = Entry(top, bd=5).place(x=60, y=150)
        B = Button(top, text="Add").place(x=100, y=100)
        top.geometry("250x250")
        top.mainloop()

Test()