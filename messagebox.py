from tkinter import *
import tkinter as tk
from tkinter import messagebox



mainWindow = tk.Tk()
mainWindow.title("Button Widget")

photo = PhotoImage(file='logo.png')

def btn_handler():
    #print("Button is clicked!")
    #messagebox.showinfo(title="InfoMB", message="tkinter is awesome")
    #messagebox.showwarning(title="InfoMB", message="tkinter is awesome")
    #messagebox.showerror(title="InfoMB", message="tkinter is awesome")
    #answer = messagebox.askokcancel(title="Question", message="Do you like python ?")
    #if answer:
    #    print("You are good")
    #else:
    #    print("You are not good")

    #answer = messagebox.askretrycancel(title="Question", message="Do you like python ?")
    #answer = messagebox.askyesno(title="Question", message="Do you like python ?")
    #answer = messagebox.askyesnocancel(title="Question", message="Do you like python ?")
    answer = messagebox.askquestion(title="Question", message="Do you like python ?")



btn_str = StringVar()

btn = Button(mainWindow, textvariable=btn_str, command=btn_handler, width=200, height=100)

btn.config(relief="raised", bd=5, bg="blue", fg="white", font=("Arial", 14), image=photo, compound="bottom")


btn_str.set("Click Button!")
#btn.pack()
btn.place(x=100, y=30)



mainWindow.geometry("800x500")
mainWindow.mainloop()
