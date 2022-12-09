from tkinter import (
    Tk, Button, PhotoImage
)

root = Tk()
root.title("sungbin GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2222222222")
btn2.pack()                         #글자수에 따라서 버튼 크기 바뀜

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444444444" )
btn4.pack()                  #크기 고정 글자수가 늘어나도 버튼크기 그대로


btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="GUI/c.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버트이 클릭되었어요")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()