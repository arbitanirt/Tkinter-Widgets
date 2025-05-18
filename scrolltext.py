import tkinter as tk
from tkinter.scrolledtext import ScrolledText

mainwindow = tk.Tk()
mainwindow.title("Scrolled Text")

stw = ScrolledText(mainwindow, bg="orange")
stw.config(fg="white", font=(None, 22))
stw.pack()


mainwindow.geometry('500x500')
mainwindow.mainloop()