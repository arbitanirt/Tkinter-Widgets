import tkinter as tk
from tkinter import *

mainwindow = tk.Tk()
mainwindow.title("Listbox")
def btn_handler():
    print(lb.curselection())
    lb.delete(lb.curselection())
    #data = lb.get(lb.curselection())
    #print("Data is : ", data)


lb = Listbox(mainwindow)
lb.insert(0, "Apple")
lb.insert(1, "Blackberry")
lb.insert(2, "Windows")
lb.insert(3, "Android")
lb.insert(3, "ABCDEFGH")

lb.insert(4, "Linux")
lb.insert(5, "Iphone")
lb.config(height=lb.size(), bg="blue", fg="white", font=(None, 20))
#lb.config(height=lb.size(), selectmode="multiple", bg="blue", fg="white", font=(None, 20))
lb.pack()


lb_btn = Button(mainwindow, text="Click Me", command=btn_handler)
lb_btn.pack()

mainwindow.geometry("500x500")
mainwindow.mainloop()