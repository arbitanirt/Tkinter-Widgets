import tkinter as tk
from tkinter import Menubutton, Menu


mainwindow = tk.Tk()
mainwindow.title("Menubutton")


mbtn = Menubutton(mainwindow, text="FileMenu", relief="groove", bd=3)

mbtn.menu = Menu(mbtn, tearoff=0)
mbtn["menu"] = mbtn.menu

def open_handler():
    print('Open button is clicked')

def save_handler():
    print('save button is clicked')

def saveas_handler():
    print('Save As button is clicked')

def check_handler():
    print('CHECK BUTTON IS CLICKED')


mbtn.menu.add_command(label="Open", command=open_handler)
mbtn.menu.add_command(label="Save", command=save_handler)
mbtn.menu.add_command(label="Save As", command=saveas_handler)
mbtn.menu.add_checkbutton(label="CheckOption", command=check_handler)

mbtn.menu.add_radiobutton(label="text")
mbtn.menu.add_radiobutton(label="pdf")
mbtn.menu.add_radiobutton(label="Mp3")




mbtn.pack()



mainwindow.geometry("500x500")
mainwindow.mainloop()