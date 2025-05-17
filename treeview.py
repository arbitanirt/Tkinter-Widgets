import tkinter as tk
from tkinter import *
from tkinter import ttk

mainwindow = tk.Tk()
mainwindow.title("Treeview")

my_table = ttk.Treeview(mainwindow, columns=("OS", "Brand", "Model"), show="headings", height=4)

my_table.heading("OS", text="OS")
my_table.heading("Brand", text="Brand")
my_table.heading("Model", text="Model")

my_table.insert('', "end", values=["Android", "Samsung", "Galaxy Core A03"])
my_table.insert('', "end", values=["IOS", "Apple", "6S"])
my_table.insert('', "end", values=["Windows", "Nokia", "Lumia"])
my_table.insert('', "end", values=["BB10", "Blackberry", "charcol"])
my_table.insert('', "end", values=["IOS", "Apple", "X"])


for column in my_table['column']:
    my_table.column(column, anchor="center")

my_table.pack()


mainwindow.geometry("900x500")
mainwindow.mainloop()