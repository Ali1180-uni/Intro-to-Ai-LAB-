from tkinter import *
window = Tk()
canvas = Canvas(window, bg="white", width=200, height=300)
canvas.pack()

def mouseCall(event):
    canvas.create_text(event.x, event.y, text="Assalam-o-Alaikum")

canvas.bind("<Button-1>", mouseCall)
window.mainloop()