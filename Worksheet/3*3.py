from tkinter import *

def three():
    batman = 3*3
    label.config(text = batman)


window = Tk()
label = Label(window, text = "0")
label.pack()
button = Button(window, text = "3 times 3", command = three)
button.pack()

window.mainloop()