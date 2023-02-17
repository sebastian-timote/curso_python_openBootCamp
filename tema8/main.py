#guardar los datos de una instancia o objeto
import pickle
class Juguete:
    nombre = ''
    precio = 0.0
    def __init__(self, nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def getNombre(self):
        return self.nombre
        
j1 = Juguete('potato',2.2)

#serializar -> convertir la representacion de un programa en una secuencia de datos que podamos escribir en un fichero
def serializacion(archivo,data):
    f = open(archivo,'wb')
    pickle.dump(data, f)#serializacion
    f.close()
#serializacion('datos.bin',j1)

def deserializacion(archivo):
    f = open(archivo,'rb')
    potato = pickle.load(f)#serializacion
    f.close()
    return potato
    
papa = deserializacion('datos.bin')
print(type(papa))
print(papa.getNombre(), 'precio: ', papa.precio)











        
        



