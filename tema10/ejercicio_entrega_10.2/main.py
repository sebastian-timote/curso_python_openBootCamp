import tkinter

window = tkinter.Tk()
from tkinter import ttk

window.title('Lista desplegable')
window.geometry('420x380+1200+100')
window.config(background='dark turquoise')
var = tkinter.StringVar(window)
var.set('pink')
opcionesColor = ['blue','pink','yellow','green', 'black', 'purple']
menuDesplegable = tkinter.OptionMenu(window, var, *opcionesColor)
menuDesplegable.config(width=20)
menuDesplegable.pack(side='left',padx=30,pady=30)
etiqueta = tkinter.Label(window, text='Color seleccionado:', bg='pink',fg='white')
etiqueta.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tkinter.X)
colores = tkinter.Label(window, bg='plum', textvariable=var, padx=5,pady=5,width=50)
colores.pack()
window.mainloop()
