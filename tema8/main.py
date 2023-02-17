# escritura de ficheros
# a -> agrega nuevo texto al final
# w -> escribe en el archivo especificado borrando lo antiguo que contenga
#f = open('mifichero.txt','w')
#f.write('datos\n')
#f.write('datos2\n')
#f.close()

#TODO escribir lineas
def escribe(archivo,data):
    f = open(archivo,'w')
    for lineas in data:
        if not lineas.endswith('\n'):
            lineas = lineas + '\n'
        f. write(lineas)
    f.close()

lista = [
    'una linea',
    'dos lineas',
    'tres lineas'
]
escribe('mifichero.txt', lista)










        
        



