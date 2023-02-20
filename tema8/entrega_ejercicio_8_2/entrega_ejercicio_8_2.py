import pickle
class Vehiculo:
    autopartsChange = ''
    precio = 0.0
    def __init__(self, partesAuto, precio):
        self.autopartsChange = partesAuto
        self.precio = precio

    def guardarRegistro(self,archivo,obj):
        #guardamos el objeto y los valores pasados paar llevar registro
        #guardamos los datos en un archivo
        f = open(f'tema8/entrega_ejercicio_8_2/{archivo}','wb')
        pickle.dump(obj,f)
        f.close()
        
    def cargarRegistro(self,archivo):
        f = open(f'tema8/entrega_ejercicio_8_2/{archivo}','rb')
        objeto = pickle.load(f)
        f.close()
        return objeto
    
    def verDatosAutopartes(self):
        print(f'la parte es: {self.autopartsChange} y cuesta: {self.precio}')


        
    

def main():
    coche = Vehiculo('bujia',18000)
    #coche.guardarRegistro('moto_Boxer.txt', coche)
    coche.verDatosAutopartes()

    dataAnterior = coche.cargarRegistro('moto_Boxer.txt')
    dataAnterior.verDatosAutopartes()

    


if __name__ == '__main__':
    main()