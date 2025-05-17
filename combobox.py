import tkinter as tk
from tkinter import ttk, StringVar



mainwindow = tk.Tk()
mainwindow.title("Combobox")

def handler_cb(event):
    print('Selected : ', myData.get())

myData = StringVar()

cb = ttk.Combobox(mainwindow, textvariable=myData)
cb["values"] = ["Apple", "Android", "IOS", "Windows", "Linux"]
cb["state"] = "readonly"

cb.bind("<<ComboboxSelected>>", handler_cb)
cb.pack()



mainwindow.geometry("500x500")
mainwindow.mainloop()