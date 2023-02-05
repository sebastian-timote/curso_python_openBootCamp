#from abc import ABC, abstractmethod

#class Animal(ABC):
#    @abstractmethod
#    def sonido(self):
#        pass

#    def diHola(self):
#        print('hola')

#class Perro(Animal):
#    def sonido(self):
#        print('guau')

#class Gato(Animal):
#    def sonido(self):
#        print('miau')


#p = Perro()
#p.sonido()
#p.diHola()
#g = Gato()
#g.sonido()

#TODO COMPOSICION UNA CLASE COMPUESTA DE OTRAS CLASES

#class Motor:
#    tipo = 'diesel'
    
#class Ventanas:
#    cantidad = 5

#    def cambiarCantidad(self,valor):
#        self.cantidad = valor
    
#class Ruedas:
#    cantidad = 4

#class Carroceria:
#    ventanas = Ventanas()
#    ruedas = Ruedas()

#class Coche:
#    motor = Motor()
#    carroceria = Carroceria()


#c = Coche()
#print('motor es', c.motor.tipo )
#print('numero de ventanas es ', c.carroceria.ventanas.cantidad )
#c.carroceria.ventanas.cambiarCantidad(6)
#print('numero de ventanas es ', c.carroceria.ventanas.cantidad )

#TODO otro ejemplo de COMPOSICION 


class Categorias:
    IdCategoria = 0
    Nombre = ''
class Proveedores:
    IdProveedor = 0
    Nombre = ''
class Productos:
    IdProducto = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoDeproducto = 0
    CIFProveedor = Proveedores()