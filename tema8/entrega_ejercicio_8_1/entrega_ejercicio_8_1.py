def main():
    def crearArchivo(nombreArchivo):
        file = open(f'tema8/entrega_ejercicio_8_1/{nombreArchivo}','xt')
        file.close()
    def editarArchivo(nombreArchivo,contenidoArchivo):
        file = open(f'tema8/entrega_ejercicio_8_1/{nombreArchivo}','a')
        file.write(contenidoArchivo)
        file.close()
    opcion = int(input('Escoger la opcion a realizar con archivos\n 1.crear archivo\n 2.editar archivo\n'))
    if opcion == 1:
        nomArchivo = str(input('ingresa el nombre del archivo a crear: '))
        crearArchivo(nomArchivo)
    elif opcion == 2:
        nomEditArchivo = str(input('ingresa el nombre del archivo a editar: '))
        contenidoArchivo = str(input('ingresa el contenido que deseas agregar al archivo: '))
        editarArchivo(nomEditArchivo, contenidoArchivo)
    else:
        print('introducir dato correcto')
if __name__ == '__main__':
    main()