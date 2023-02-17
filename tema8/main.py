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
#busca en una archivo del sistema lo recorre y agrega en una lista los user
# y lo simprime en la terminal
def main():
    usuarios = listarUsuario()
    print(usuarios)
    for user in usuarios:
        print(f'Usuario: {user}')
def listarUsuario():
    f = open('/../../../etc/passwd', 'r')
    datos = f.readlines()
    f.close()
    resultado = []
    for linea in datos:
        if ((linea.startswith('sys') == True) or (linea[0] == '_')):
            continue
        partes = linea.split(':')
        resultado.append(partes[0])
    return resultado


    
if __name__ == '__main__':
    main()







        
        



