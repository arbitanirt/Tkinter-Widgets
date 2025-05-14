import tkinter as tk
from tkinter import *

mainWindow = tk.Tk()
mainWindow.title("Display Method")

#lw = Label(mainWindow, text="Label1", relief="raised", bd=2)
#lw.pack()

#lw2 = Label(mainWindow, text="Label2", relief="raised", bd=2)
#lw2.pack()

#lw = Label(mainWindow, text="Label1", relief="raised", bd=2)
#lw.grid(row=0, column=0)

#lw2 = Label(mainWindow, text="Label2", relief="raised", bd=2)
#lw2.grid(row=1, column=1)

#lw3 = Label(mainWindow, text="Label3", relief="raised", bd=2)
#lw3.grid(row=1, column=0)


lw2 = Label(mainWindow, text="Label1", relief="raised", bd=2)
lw2.place(x=500, y=0)

mainWindow.geometry("600x400")
mainWindow.mainloop()
