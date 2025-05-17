import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("Scale Widget")

#def scale_handler(value):
#    print(value)

def scale_handler(value):
    btn.config(text="Range : " + str(value))

s = Scale(mainwindow, from_=200, to=500, length=300, orient=HORIZONTAL, command=scale_handler, bg="blue", troughcolor='green', fg='white', font=(None, 22))
s.set(350)
s.pack()

def btn_handler():
    btn.config(text="Range : " + str(s.get()))

btn = Button(mainwindow, text="Get Scale Data", command=btn_handler)
btn.pack()

mainwindow.geometry("500x500")
mainwindow.resizable(False, False)
mainwindow.mainloop()