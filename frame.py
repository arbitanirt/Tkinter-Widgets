import tkinter as tk
from tkinter import *

mainwindow = tk.Tk()
mainwindow.title("Frame")

#fm = Frame(mainwindow, bg="orange", width=400, height=400)
fm = Frame(mainwindow, bg="orange", width=300, height=300)

l1 = Label(fm, text="Login")
l1.place(x=100, y=10)

e1 = Entry(fm)
e1.place(x=170, y=10)

l2 = Label(fm, text="Password")
l2.place(x=100, y=40)

e2 = Entry(fm,show="*")
e2.place(x=170, y=40)

b1 = Button(fm, text="Submit")
b1.place(x=100, y=150)



fm.place(x=10, y=50)


mainwindow.geometry("500x500")
mainwindow.mainloop()