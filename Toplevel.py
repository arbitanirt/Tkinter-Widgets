import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("Toplevel Experiment")

def btn_handler():
    tp = Toplevel()
    tp.title("Toplevel Window")
    tp.geometry('200x200')
    tp.resizable(False, False)


btn = Button(mainwindow, text="Open new window", command=btn_handler)
btn.pack()

mainwindow.geometry("500x500")
mainwindow.mainloop()