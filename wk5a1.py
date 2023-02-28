# Create a digital clock app
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(Text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('ds-digital', 80), background='pink',
    foreground='white')
lbl.pack(anchor='center')
time()
mainloop()
