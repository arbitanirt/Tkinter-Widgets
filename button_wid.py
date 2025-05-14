from tkinter import *
import tkinter as tk



mainWindow = tk.Tk()
mainWindow.title("Button Widget")

photo = PhotoImage(file='logo.png')

def btn_handler():
    print("Button is clicked!")

btn_str = StringVar()

btn = Button(mainWindow, textvariable=btn_str, command=btn_handler, width=200, height=100)

btn.config(relief="raised", bd=5, bg="blue", fg="white", font=("Arial", 14), image=photo, compound="bottom")


btn_str.set("Click Button!")
#btn.pack()
btn.place(x=100, y=30)



mainWindow.geometry("800x500")
mainWindow.mainloop()
