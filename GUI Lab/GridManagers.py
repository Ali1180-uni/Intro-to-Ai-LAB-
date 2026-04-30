from tkinter import *
class GridManager:
    window = Tk()
    window.title("Grid Manager DEMO")
    message = Message(window, text="This is a messsage wiget occupies row and two columns")
    message.grid(row=1, column=1,rowspan=3, columnspan=2)
    Label(window, text="FirstName").grid(row=1, column=3)
    Entry(window).grid(row=1, column=4, padx=5, pady=5)
    Label(window, text="LastName").grid(row=2, column=3)
    Entry(window).grid(row=2, column=4)
    Button(window, text="Get Name").grid(row=3, column=4, padx=5, pady=5, sticky=E)
    window.mainloop()

    
GridManager()