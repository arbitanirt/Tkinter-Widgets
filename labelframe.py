import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("labelFrame")


lbf = LabelFrame(mainwindow, text="Login Credential", relief="groove", bd=4, width=480, height=200, bg="blue")

lb = Label(lbf, text="Username", width=50, height=2)
lb.pack()

lb2 = Label(lbf, text="Email ID", width=50, height=2)
lb2.pack()

lbf.pack()


mainwindow.geometry("500x500")
mainwindow.mainloop()