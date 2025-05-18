import tkinter as tk
from tkinter import *

mainwindow = tk.Tk()
mainwindow.title('Spinbox')

def spinbox_handler():
    print("SpinBox value is changed! ", sb.get())

sb = Spinbox(mainwindow, from_=0, to=20, state='readonly', command=spinbox_handler)
#sb.config(state='readonly')
sb.config(fg="blue", font=(None, 24))
sb.pack()

mainwindow.geometry('500x500')
mainwindow.mainloop()



mainwindow.geometry('500x500')
mainwindow.mainloop()