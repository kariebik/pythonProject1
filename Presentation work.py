from tkinter import *
def vote_counter(x, vot_num):
    if x.count("A") + x.count("B") != vot_num:
        raise ValueError
    if x.count("A") > x.count("B"):
        print("A")
    elif x.count("A") < x.count("B"):
        print("B")
    elif x.count("A") == x.count("B"):
        print("Tie")

window = Tk()
window.title("Vote counter")

label = Label(window, text = "Welcome to Python")
tt = Entry(window)
zz = Entry(window)
button = Button(window, text = "Click Me")
eval(tt.pack())
label.pack()
eval(zz.pack())
try:
    vote_counter(zz, tt).pack()
except ValueError:
    print("The number of votes entered isn't equal to the number of votes")
button.pack()


window.mainloop()