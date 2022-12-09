from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar
)
from tkinter.ttk import Combobox

root = Tk()
root.title("sungbin GUI")
root.geometry("640x480")

values = [str(i) + "day" for i in range(1, 32)]
Combobox = Combobox(root, height=5, values=values)
Combobox.pack()
Combobox.set("select card pay day")




def btncmd():
    pass

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()


