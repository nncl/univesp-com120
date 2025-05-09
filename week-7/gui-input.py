from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def on_click():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))

root = Tk()

label = Label(root, text='Type some date')
label.grid(row=0, column=0)

entry = Entry(root)
entry.grid(row=0, column=1)

button = Button(root, text='Submit', command=on_click)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()
