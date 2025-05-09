from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime

def on_click():
    time = strftime('Day: %d %b %Y \nTime: %H:%M:%S %p\n', localtime())
    showinfo("Time", time)

root = Tk()

button = Button(root, text='Click here', command=on_click)
button.pack()

root.mainloop()