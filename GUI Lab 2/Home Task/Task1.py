from tkinter import *

class MenuDemo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator Menu")
        
        # Menu Setup
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operation", menu=operationMenu)
        operationMenu.add_command(label="Add", command=self.add)
        operationMenu.add_command(label="Subtract", command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply", command=self.multiply)
        operationMenu.add_command(label="Divide", command=self.divide)

        self.frame1 = Frame(self.window, padx=10, pady=10)
        self.frame1.pack()
        
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.v3 = StringVar()

        Label(self.frame1, text="Num 1:").grid(row=0, column=0)
        self.e1 = Entry(self.frame1, width=10, textvariable=self.v1, justify=RIGHT)
        self.e1.grid(row=0, column=1, padx=5)

        Label(self.frame1, text="Num 2:").grid(row=1, column=0)
        self.e2 = Entry(self.frame1, width=10, textvariable=self.v2, justify=RIGHT)
        self.e2.grid(row=1, column=1, padx=5)

        Label(self.frame1, text="Result:").grid(row=2, column=0)
        Entry(self.frame1, width=10, textvariable=self.v3, justify=RIGHT, state='readonly').grid(row=2, column=1, padx=5)

        self.frame2 = Frame(self.window)
        self.frame2.pack(pady=5)
        for op in [("Add", self.add), ("Sub", self.subtract), ("Mul", self.multiply), ("Div", self.divide)]:
            Button(self.frame2, text=op[0], command=op[1], width=5).pack(side=LEFT, padx=2)

        self.frame3 = Frame(self.window, pady=10)
        self.frame3.pack()
        
        nums = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]
        for idx, i in enumerate(nums):
            row, col = divmod(idx, 3)
            Button(self.frame3, text=str(i), width=5, height=2, 
                   command=lambda x=i: self.input_number(x)).grid(row=row, column=col, padx=2, pady=2)
        
        # Clear Button
        Button(self.frame3, text="C", width=5, height=2, bg="orange", 
               command=lambda: [self.v1.set(""), self.v2.set(""), self.v3.set("")]).grid(row=3, column=1, columnspan=2, sticky="we")

        self.window.mainloop()

    def input_number(self, num):
        current_focus = self.window.focus_get()
        if current_focus == self.e2:
            self.v2.set(self.v2.get() + str(num))
        else:
            self.v1.set(self.v1.get() + str(num))

    def add(self): self.v3.set(float(self.v1.get()) + float(self.v2.get()))
    def subtract(self): self.v3.set(float(self.v1.get()) - float(self.v2.get()))
    def multiply(self): self.v3.set(float(self.v1.get()) * float(self.v2.get()))
    def divide(self): 
        try: self.v3.set(round(float(self.v1.get()) / float(self.v2.get()), 2))
        except ZeroDivisionError: self.v3.set("Error")

MenuDemo()
