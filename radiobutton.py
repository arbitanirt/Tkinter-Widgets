import tkinter as tk
from tkinter import *


mainwindow = tk.Tk()
mainwindow.title("Radiobutton")

rbtn_image = PhotoImage(file="logo.png")

def rbtn_handler():
    print("Invoked", myData.get())

myData = StringVar()
myData.set("Java")

#rbtn = Radiobutton(mainwindow, text="Python", value="Python", command=rbtn_handler, variable=myData)
#rbtn.pack()

#rbtn2 = Radiobutton(mainwindow, text="Java", value="Java", command=rbtn_handler, variable=myData)
#rbtn2.pack()

for i in range(5):
    rbtn = Radiobutton(mainwindow, text="Python_" + str(i+1), value=str(i+1), command=rbtn_handler, variable=myData, width=200, relief='raised')
    rbtn.config(bg="blue",
                bd=3,
                height=150,
                image=rbtn_image,
                compound="top",
                fg="white",
                font=("Arial", 22)
                )
    rbtn.pack()

mainwindow.geometry("500x500")
mainwindow.mainloop()