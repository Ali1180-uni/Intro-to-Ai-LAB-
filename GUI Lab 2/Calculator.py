from tkinter import *
class MenuDemo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Menu Demo")
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operation", menu=operationMenu)
        operationMenu.add_command(label="Add", command=self.add)
        operationMenu.add_command(label="Subtract", command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply", command=self.multiply)
        operationMenu.add_command(label="Divide", command=self.divide)
        exitMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Exit", menu=exitMenu)
        exitMenu.add_command(label="Quit", command=self.window.quit)
        self.frame1 = Frame(self.window)
        self.frame1.grid(row=1, column=1, pady=10)
        Label(self.frame1, text="Number 1").pack(side=LEFT)
        self.v1 = StringVar()
        Entry(self.frame1, width= 5, textvariable=self.v1, justify=RIGHT).pack(side=LEFT)
        Label(self.frame1, text="Number 2").pack(side=LEFT)
        self.v2 = StringVar()
        Entry(self.frame1, width= 5, textvariable=self.v2, justify=RIGHT).pack(side=LEFT)
        Label(self.frame1, text="Result").pack(side=LEFT)
        self.v3 = StringVar()
        Entry(self.frame1, width= 5, textvariable=self.v3, justify=RIGHT).pack(side=LEFT)
        self.window.mainloop()

    def add(self):
        print("Add")
    def subtract(self):
        print("Subtract")
    def multiply(self):
        print("Multiply")
    def divide(self):
        print("Divide")

MenuDemo()
