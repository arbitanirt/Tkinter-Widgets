import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("TextWidget Use")

tw = Text(mainwindow, width=50, height=10)
tw.config(bg="yellow", fg="green", font=(None, 20))
tw.place(x=10, y=10)

def btn_handler():
    #print(tw.get("2.0", "end"))
    tw.insert("end", "PYTHON\n")

btn = Button(mainwindow, text="Set", command=btn_handler)
btn.place(x=10, y=350)


def btn_handler2():
    #print(tw.get("2.0", "end"))
    tw.delete("1.0", "end")

btn2 = Button(mainwindow, text="Delete", command=btn_handler2)
btn2.place(x=100, y=350)


mainwindow.geometry("900x500")
mainwindow.mainloop()