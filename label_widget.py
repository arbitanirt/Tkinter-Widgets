import tkinter
from tkinter import Label, PhotoImage, StringVar
import tkinter as tk

mainwindow = tk.Tk()
mainwindow.title("Label Widget")
photo = PhotoImage(file="logo.png")

myVar = StringVar()
lw = Label(mainwindow,
           #text="Label",
           textvariable=myVar,
           bd=2,
           relief="groove",
           width=20,
           height=3,
           #anchor="center",
           #image=photo,
           #compound="left",
           #fg="blue",
           #bg="red",
           #font=("Times new roman", 20, "bold"),
           #justify="center",
           #padx=50,
           #pady=20,
           #"underline=3
           )

lw.config(
            anchor="center",
            fg="blue",
            font=("Times new roman", 20, "bold"),
            padx=50,
            pady=20,
            state="normal",
)

lw.pack()

myVar.set("Random Text")

mainwindow.geometry("800x600")
mainwindow.mainloop()