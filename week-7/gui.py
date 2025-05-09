from tkinter import Tk, Label, PhotoImage

root = Tk(className='Hello world')

label = Label(master=root, text='Hello world', font=("Courier", 26))
label.pack(side='bottom')

photo = PhotoImage(file='homer.gif').subsample(5)
image = Label(master=root, image=photo, width=300, height=300)
image.pack(side='top')

root.mainloop()