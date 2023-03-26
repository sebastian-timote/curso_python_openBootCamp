from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ['pepe','maria','ernesto','ruben','carlos','laura','ana', 'lorena']:
    listbox.insert(END, item)
listbox.pack()
label = Label(text='Lista de nombres de personas')
label.pack()
master.mainloop()
