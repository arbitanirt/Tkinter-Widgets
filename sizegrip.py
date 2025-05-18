import tkinter as tk
from tkinter import ttk


mainwindow = tk.Tk()
mainwindow.title('Sizegrip')

sg = ttk.Sizegrip(mainwindow)
sg.pack(side='right', anchor='se')



mainwindow.geometry('500x500')
mainwindow.mainloop()