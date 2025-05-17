import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
import time

mainwindow = tk.Tk()
mainwindow.title("Progressbar")

def btn_handler():
    for i in range(1,10):
        pb['value'] = i*10
        time.sleep(0.2)
        mainwindow.update_idletasks()

btn = Button(mainwindow, text="Start", command=btn_handler, orient="vertical")
btn.pack()


pb = Progressbar(mainwindow, length=250)
pb.pack()



mainwindow.geometry("500x500")
mainwindow.mainloop()