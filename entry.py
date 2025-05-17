import tkinter as tk
from tkinter import *

mainwindow = tk.Tk()
mainwindow.title("Entry Widget Example")



entry = Entry(mainwindow, relief="groove", bd=5)
entry.config(font=(None, 22))
#entry.config(font=(None, 22), show="*")
entry.pack()

def btn_handler():
    btn.config(text=entry.get())

btn = Button(mainwindow, text="Get Data", command=btn_handler)
btn.pack()

def btn_handler2():
    entry.delete(0, END)

btn2 = Button(mainwindow, text="Delete", command=btn_handler2)
btn2.pack()


mainwindow.geometry("500x500")
mainwindow.mainloop()