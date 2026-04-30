from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton = Button(frame, text="Red", fg="red").pack(side=LEFT)
greenbutton = Button(frame, text="Green", fg="green").pack(side=LEFT)
bluebutton = Button(frame, text="Blue", fg="blue").pack(side=LEFT)
blackbutton = Button(bottomframe, text="Black", fg="black").pack(side=BOTTOM)

root.mainloop()