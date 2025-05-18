import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("Scrollbar Window")

scb = Scrollbar(mainwindow)
scb.pack(side="right", fill="y")


tw = Text(mainwindow, yscrollcommand=scb.set)
tw.config(width=60, height=12)
tw.pack()

scb.config(command=tw.yview)

mainwindow.geometry('500x200')
mainwindow.mainloop()