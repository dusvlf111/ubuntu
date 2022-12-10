from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar
)
from tkinter.ttk import (
    Progressbar, Combobox
    )


root = Tk()
root.title("sungbin GUI")
root.geometry("640x480") #가로 x 세로


                                                #결정되지 않은 값
# progressbar = Progressbar(root, maximum=100, mode='indeterminate') 
progressbar = Progressbar(root, maximum=100, mode='determinate') 
# progressbar.start(10) # 10 ms 마다 움직임
progressbar.start(10) # 1 ms 마다 움직임
progressbar.pack()





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


