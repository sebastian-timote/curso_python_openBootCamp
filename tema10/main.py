# el run de vs code no funciono toco ejecutarlo directo de consola de linux
#pack -> se utiliza cuando se quiere situar elementos de arriba abajo
# o de izq a der
#bg ->background
#fg ->foreground
#fill-> llenar un espacio en el eje x, y o both
#expand-> expande y lo deja en el centro
#side -> lo posiciona a la izq o derecha
import tkinter
window = tkinter.Tk()

#label_saludo = tkinter.Label(window, text="hola!", bg="yellow", fg="blue")# creo etiqueta
#label_saludo.pack(ipadx=50,ipady=50, fill='x')#posiciono mi etiqueta dentro de la ventana
#label_saludo.pack(ipadx=50,ipady=50, side='left')#posiciono mi etiqueta dentro de la ventana

#label_adios = tkinter.Label(window, text="Adios", bg="red",fg="white")
#label_adios.pack(fill='both',expand=True)
#label_adios.pack(fill='both',side='right')

#TODO EJEMPLO DOS

#label1 = tkinter.Label(window, text="label1", bg="yellow",fg="blue")
#label1.pack(ipadx=45,ipady=15, fill='x')

#label2 = tkinter.Label(window, text="label2", bg="purple",fg="white")
#label2.pack(ipadx=45,ipady=15, fill='x')

#label3 = tkinter.Label(window, text="label3", bg="blue",fg="white")
#label3.pack(ipadx=45,ipady=15, fill='x')

#label4 = tkinter.Label(window, text="label4", bg="red",fg="white")
#label4.pack(ipadx=15,ipady=15, side="left")

#label5 = tkinter.Label(window, text="label5", bg="yellow",fg="black")
#label5.pack(ipadx=15,ipady=15, side="left")

#label6 = tkinter.Label(window, text="label6", bg="green",fg="white")
#label6.pack(ipadx=15,ipady=15, side="right")

##TODO GEOMETRIA GRIP
##maneja posicionamiento como una hoja de excel
##(0,0) (1,0) (2,0)
##(0,1) (1,1) (2,1)
##(0,2) (1,2) (2,2)
##(0,3) (1,3) (2,3)
##sticky-> para que la label quede fija
## padx -> es como un padding en css
## ipadx -> es como un margin en css
##TODO EJEMPLO GRIP
from tkinter import ttk
#window.columnconfigure(0,weight=3)
#window.rowconfigure(1, weight=3)
##usuario
##etiqueta usuario
#username_label = ttk.Label(window, text="username:")
#username_label.grid(column=0,row=0, sticky=tkinter.W, padx=5, pady=5)
##campo usuario
#username_entry = ttk.Entry(window)
#username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)
##password
##etiqueta contraseña
#password_label = ttk.Label(window, text="password:")
#password_label.grid(column=0,row=1, sticky=tkinter.W, padx=5, pady=5)
##campo contraseña
#password_entry = ttk.Entry(window, show="*")
#password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)
##boton login
#login_button = ttk.Button(window, text="login")
#login_button.grid(column=2, row=2, sticky=tkinter.E, padx=5, pady=5) 
##TODO FIN EJEMPLO GRIP

##TODO GEOMETRIA PLACE
## posicionamiento absoluto -> no se mueve asi cambie de resolucion el tamaño de la aplicacion
## posicionamiento relativo -> cambia deacuerdo el tamano de la aplicacion

#label1 = ttk.Label(window, text="posicionamiento absoluto", background="blue", foreground="white")
#label1.place(x=10,y=50)

#label2 = ttk.Label(window, text="posicion relativa", background="red", foreground="yellow")
#label2.place(relx=0.10,rely=0.15, relwidth=0.5, anchor="ne")

##TODO EJEMPLO PLACE
import random

colors = ['blue','red','yellow','purple','black']

for x in range(0,10):
    color = random.randint(0, len(colors)-1 )
    color2 = random.randint(0, len(colors)-1 )
    label = ttk.Label(window, text="etiqueta!!", background=colors[color], foreground=colors[color2])
    label.place(x=random.randint(0,100),y=random.randint(0,100))

##TODO FIN EJEMPLO PLACE

window.mainloop()#para que se pueda ver la ventana se tiene que poner un main loop

