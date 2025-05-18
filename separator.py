import tkinter as tk
from tkinter import ttk, Label

mainwindow = tk.Tk()
mainwindow.title('Separator')

l1 = Label(mainwindow, text='Label 1')
l1.place(x=10, y=10)

#sp = ttk.Separator(mainwindow, orient='horizontal')
#sp.place(x=10, y=100, width=480)

sp = ttk.Separator(mainwindow, orient='vertical')
sp.place(x=200, y=10, height=480)

#l2 = Label(mainwindow, text='Label 2')
#l2.place(x=10, y=150)

l2 = Label(mainwindow, text='Label 2')
l2.place(x=300, y=10)

mainwindow.geometry('500x500')
mainwindow.mainloop()
