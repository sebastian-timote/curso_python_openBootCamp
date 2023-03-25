## en este ejercicio teneis que crear una lista de radiobutton que muestre 
## la opcion que se ha seleccionado y que contenga un boton de reinicio para que
## deje todo como al principio. al principio no debe haber una opcion seleccionada
import os
import sys
import tkinter
from tkinter import messagebox
ventana = tkinter.Tk()
from tkinter import ttk
def mostrarOpcion(event):
    s = seleccionado.get()
    messagebox.showinfo(title='seleccion',message='seleccionaste la opcion ' + s)

def salir(event):
    ##para reiniciar aplicacion 
    os.execl(sys.executable, sys.executable, * sys.argv)

ventana.geometry("500x300+0+0")
ventana.title('que opcion seleccionaste')
#sys.exit(0)
seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(ventana, text="opcion1", value='1', variable=seleccionado)
r2 = ttk.Radiobutton(ventana, text="opcion2", value='2', variable=seleccionado)
r3 = ttk.Radiobutton(ventana, text="opcion3", value='3', variable=seleccionado)
r4 = ttk.Radiobutton(ventana, text="opcion4", value='4', variable=seleccionado)
r5 = ttk.Radiobutton(ventana, text="opcion5", value='5', variable=seleccionado)

r1.grid(column=0,row=0, padx=5,pady=5)
r2.grid(column=0,row=1, padx=5,pady=5)
r3.grid(column=0,row=2, padx=5,pady=5)
r4.grid(column=0,row=3, padx=5,pady=5)
r5.grid(column=0,row=4, padx=5,pady=5)

botonEnter = tkinter.Button(ventana, text='Enter')
botonEnter.grid(column=1,row=4, padx=100,pady=5,ipadx=50)
botonEnter.bind('<Button-1>',mostrarOpcion)

botonSalir = tkinter.Button(ventana, text='Salir')
botonSalir.grid(column=1,row=5, padx=100,pady=5,ipadx=50)
botonSalir.bind('<Button-1>',salir)





#print('hola que mas pues bebe')
ventana.mainloop()