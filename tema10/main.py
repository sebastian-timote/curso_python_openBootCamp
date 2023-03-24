
import sys
import tkinter

window = tkinter.Tk()
from tkinter import ttk
##TODO FRAME --> AGRUPACION DE COSAS, PARECE UN DIV
##crear el frame
#frame = ttk.Frame(window)
#frame2 = ttk.Frame(window)
## crear etiqueta
#label = ttk.Label(frame, text="usando frame")
#label2 = ttk.Label(frame2, text="frame dos")
##ubicar la etiqueta
#label.grid(column=0,row=0, sticky=tkinter.W, padx=50,pady=50)
#label2.grid(column=0,row=1,sticky=tkinter.E, padx=50, pady=50)

##ubicar los frame
#frame.grid(column=0,row=0, sticky=tkinter.W)
#frame2.grid(column=0,row=1, sticky=tkinter.W)

##TODO LIST BOX --> LISTA DE SELECCION

#lista = ['windows','macOS','linux', 'msDOS','amigaOS', 'beOS', 'OS/2']
#lista_items = tkinter.StringVar(value=lista) #para convertir la lista a un formato que entienda ttk o tcl
#listBox = tkinter.Listbox(window, height=60, listvariable=lista_items)
#listBox.grid(column=0,row=0, sticky=tkinter.W)

##TODO RADIOBUTTON --> 
#def miFuncion():
#    print('clicado')
#seleccionado = tkinter.StringVar()# agrupa un radio button de otro
##sitodos tiene esta misma variable solo se podra escoger uno de ellos 
#r1 = ttk.Radiobutton(window, text="Si", value='1', variable=seleccionado, command=miFuncion)
#r2 = ttk.Radiobutton(window, text="No", value='2', variable=seleccionado)
#r3 = ttk.Radiobutton(window, text="Tal vez", value='3', variable=seleccionado)

#r1.grid(column=0,row=1, padx=5,pady=5)
#r2.grid(column=0,row=2, padx=5,pady=5)
#r3.grid(column=0,row=3, padx=5,pady=5)

#seleccionado2 = tkinter.StringVar()
#rs1 = ttk.Radiobutton(window, text="Si", value='12', variable=seleccionado2)
#rs1.grid(column=1,row=0, padx=5,pady=5)

##TODO EVENTOS ->son reacciones a una accion exterior como el teclado, mouse, etc
## <Button-1> -> evento de click izquierdo
## <Double-1> -> evento de doble click
## <Motion> -> evento cuadno el mouse pasa sobre èl
##TODO EJEMPLO 1 DE EVENTOS
#def saludar(event):
#    print('han hecho click en saludar')
#def saludarDoubleClick(event):
#    print('han hecho doble click en saludar')

#def salir(event):
#    print('adios')
#    window.quit()

#boton = tkinter.Button(window, text='Haz click')
#boton.pack()
#boton.bind('<Button-1>',saludar)#unir un evento a una accion
#boton.bind('<Double-1>',saludarDoubleClick)#evento de doble click

#botonSalir = tkinter.Button(window, text='Salir')
#botonSalir.pack()
#botonSalir.bind('<Button-1>',salir)#unir un evento a una accion
##TODO FIN EJEMPLO 1 DE EVENTOS

## TODO EJEMPLO2 EVENTOS
#def motion(event):
#    print('mouse position: (%s %s)' % (event.x, event.y))
#    return

#texto= "demo de texto en un widget msg para ver el movimiento del mouse"
#msg = tkinter.Message(window, text= texto)
#msg.config(bg='lightgreen', font=('times', 24, 'italic'))
#msg.bind('<Motion>', motion)
#msg.pack()
## TODO fin ejemplo 2 eventos

##TODO otros tipos de ventanas
from tkinter import filedialog
from tkinter import colorchooser

## me abre una ventana para cargar un archivo
#filename = filedialog.askopenfilename()

colorchooser.askcolor(initialcolor="#fff")

window.mainloop()#para que se pueda ver la ventana se tiene que poner un main loop
sys.exit(0)
