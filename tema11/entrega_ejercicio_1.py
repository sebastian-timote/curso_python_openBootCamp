#en este ejjercicio tendreis que crear una tabla llamada Alumnos que constara de tres columnas:
# la columna id de tipo entero, la columna nombre que sera de tipo texto y
# la columna apellido que tambien sera de tipo texto
# una vez creada la tabla, hay que insertarle almenos 8 alumnos 
# por ultimo tienes que realizar una busqueda de un alumno por nombre y mostrar
# los datios por consola
import tkinter
import sqlite3

window = tkinter.Tk()
from tkinter import END, ttk
def opInsert(event):
    data_nombre = label_nombre_entry.get()
    data_apellido = entry_apellido_insert.get()
    id_actual = buscarCantidadDatos()
    print(id_actual)
    id_actual=id_actual + 1
    print(id_actual)
    conn = sqlite3.connect('db_tema_11.db')
    cursor = conn.cursor()
    query = f"INSERT INTO alumnos(id,nombre,apellido)  VALUES(?,?,?)"
    rows= cursor.execute(query, (id_actual,data_nombre,data_apellido))
    print(type(rows))
    conn.commit()
    cursor.close()
    conn.close()
def opSelect(event):
    data_nombre_select = entry_nombre_select.get()
    conn = sqlite3.connect('db_tema_11.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM alumnos WHERE nombre='{data_nombre_select}'"
    rows= cursor.execute(query)
    data = rows.fetchone()
    if (data == None):
        listbox.insert(END, "registro NO existe en db")
    else:
        for item in data:
            listbox.insert(END, item)
        

        
    cursor.close()
    conn.close()

def buscarCantidadDatos():
    conn = sqlite3.connect('db_tema_11.db')
    cursor = conn.cursor()
    query = f"SELECT id FROM alumnos"
    rows= cursor.execute(query)
    print(rows)
    data = rows.fetchall()
    id = len(data)
    print("data es:",id)
    cursor.close()
    conn.close()
    return id
    
#creacion label frames
window.geometry("540x400+0+0")
window.title('interactuando con sqlite3 y tkinter')
label_insert = tkinter.LabelFrame(window,text="INSERTAR DATOS",background="lightgray",foreground="black")
label_select = tkinter.LabelFrame(window,text="VER DATOS",background="lightgray",foreground="black")
label_data = tkinter.LabelFrame(window,text="DATOS", background="lightgray",foreground="black")

#ubicacion labels frames
label_insert.grid(column=0,row=0, ipadx=5, ipady=15)
label_select.grid(column=1,row=0, ipadx=10, ipady=20)
label_data.grid(column=0,row=1, ipadx=5, ipady=5)


#label nombre
label_nombre_insert = tkinter.Label(label_insert,text="nombre",background="lightgray",foreground="black")
label_nombre_insert.grid(column=0,row=0,ipadx=5, ipady=5)

dato_input_nombre = tkinter.StringVar()
label_nombre_entry = ttk.Entry(label_insert)
label_nombre_entry.grid(column=1,row=0, ipadx=5, ipady=5,padx=5,pady=5)

label_apellido_insert = tkinter.Label(label_insert,text="apellido",background="lightgray",foreground="black")
label_apellido_insert.grid(column=0,row=1, ipadx=5, ipady=5)

entry_apellido_insert = ttk.Entry(label_insert)
entry_apellido_insert.grid(column=1,row=1, ipadx=5, ipady=5,padx=5,pady=5)

boton_enviar_insert = ttk.Button(label_insert, text="enviar")
boton_enviar_insert.grid(column=1,row=2, ipadx=5, ipady=5)


#label ver datos
label_nombre_select = tkinter.Label(label_select,text="nombre",background="lightgray",foreground="black")
label_nombre_select.grid(column=0,row=0, ipadx=5, ipady=5)

entry_nombre_select  = ttk.Entry(label_select)
entry_nombre_select.grid(column=1,row=0, ipadx=5, ipady=5,padx=5,pady=5)
boton_ver_select = ttk.Button(label_select, text="ver datos")
boton_ver_select.grid(column=1,row=3, ipadx=5, ipady=5, padx=15,pady=15)

boton_enviar_insert.bind('<Button-1>',opInsert)
boton_ver_select.bind('<Button-1>',opSelect)

#label_data_db = tkinter.Label(label_data,text="hola",background="lightgray",foreground="black")
#label_data_db.grid(column=0,row=0,ipadx=5, ipady=5)

listbox = tkinter.Listbox(label_data)
listbox.grid(column=0,row=0,ipadx=5, ipady=5)







window.mainloop()