# TODO conjunto de funciones de manipulacion de ficheros
# r: lectura
# a: append
# w: escritura
# x: create

#t: texto plano
#b: archivo binario

#+:
#f = open('/../../../etc/passwd', 'r')
#datos = f.read()# si adentro se le coloca un valor numerico seria la cantidad de caracteres que queremos leer
#datos = f.readline()# lee la primera linea
#datos = f.readline()# lee la segunda linea
#f.close()
#print(datos)
#TODO RECORRER UN ARCHIVO Y LEER LO LINEA POR LINEA
#datos = None
#while(datos != ""):
#    datos = f.readline()
#    print(datos)
#f.close()

#TODO LEE LOS DATOS Y LOS PONE EN UNA LISTA

#datos = f.readlines()
#print(datos[1])
#f.close()

#TODO OTRO EJEMPLO DE LECTURA DE FICHEROS

def main():
    usuarios = listarUsuario()
    #print(usuarios)
def listarUsuario():
    f = open('/../../../etc/passwd', 'r')
    datos = f.readlines()
    f.close()

    for linea in datos:
        if linea[0] == '/usr/':
            continue
        print(linea)
    
if __name__ == '__main__':
    main()







        
        



