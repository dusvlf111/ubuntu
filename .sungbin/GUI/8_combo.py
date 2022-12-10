from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar
)
from tkinter.ttk import Combobox

root = Tk()
root.title("sungbin GUI")
root.geometry("640x480")

values = [str(i) + "day" for i in range(1, 32)]
combobox = Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("select card pay day")

values = [str(i) + "day" for i in range(1, 32)]
read_Combobox = Combobox(root, height=10, values=values, state = "readonly")
read_Combobox.current(0)
read_Combobox.pack()






def btncmd():
    print(combobox.get())
    print(read_Combobox.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()


