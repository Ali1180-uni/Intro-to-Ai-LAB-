from tkinter import *
root = Tk()
b = 0
for i in range(5):
    for c in range(5):
        btn = Button(
            root,
            text=str(b),
            fg="white",
            bg="black", 
            activebackground="green", 
            activeforeground="blue", 
            width=6, 
            height=2, 
            borderwidth=2, 
            relief="raised", 
            font=("Arial", 12, "bold")
            )
        btn.grid(row=i, column=c)
        b = b + 1
root.mainloop()