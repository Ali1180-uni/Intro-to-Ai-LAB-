from tkinter import *
from tkinter import messagebox
def processOK():
    print("Iam ok")

def processCancel():
    messagebox.showinfo("cancel Message", "This is Cancel")

window = Tk()
window.geometry("400x300")
label1 = Label(window, text="Welcome to my App")
label1.pack()

button1 = Button(window, text="OK", bg="green", fg="white", command=processOK)
button1.pack()

button2 = Button(window, text="Cancel", bg="red", fg="white", command=processCancel)
button2.pack()

window.mainloop()