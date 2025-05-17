import tkinter as tk
from tkinter import *

mainwindow = tk.Tk()
mainwindow.title("Checkbutton")

def cbtn_handler():
    print("Fonction is invoked : ", myData.get())

image = PhotoImage(file="logo.png")
myData = StringVar()
myData.set("No")

cbtn = Checkbutton(mainwindow, text="Do you like python ?", command=cbtn_handler, variable=myData, onvalue="Yes", offvalue="No", bg="blue", fg="white", font=("Arial", 22), image=image, compound="right", relief='raised', bd=4, height=4)
cbtn.pack()

mainwindow.geometry("500x500")
mainwindow.mainloop()