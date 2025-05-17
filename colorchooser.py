import tkinter as tk
from tkinter import *
from tkinter import colorchooser

mainwindow = tk.Tk()
mainwindow.title("Color Chooser")

def btn_handler():
    color = colorchooser.askcolor(color="blue", title="Pick Any Color")
    btn.config(bg=color[1])
    print("COLOR : ", color)

btn = Button(mainwindow, text="choose a color", command=btn_handler)
btn.pack()





mainwindow.geometry("500x500")
mainwindow.mainloop()