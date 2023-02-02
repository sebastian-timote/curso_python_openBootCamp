#POO
#TODO ejemplo clases dinamicas
#class Dino:
#    _encendido = True
#    def apaga(self):
#        self._encendido = False
#    def enciende(self):
#        self._encendido = True
#    def isEncendido(self):
#        return self._encendido

#la instancia d es un espacio de memoria diferente a d2
#por eso tienen resultados diferentes
#d = Dino()
#d.apaga()
#print(d.isEncendido())

#d2 = Dino()
#d2.enciende()
#print(d2.isEncendido())
# por convencion de programadores no deberiamos modificar un metodo o variable cuando tenga guion abajo antes
#self-> podemos modificar el valor de una variable de la clase(global) ya que si no lo ponemos creamos una nueva variable con el mismo nombre del ambito del metodo

#TODO ejemplo clases estaticas
#una clase estatica no se le pueden crear diferentes instancias
# solo toma un espacio de memoria 
# en una clase dinamica cada instancia toma su espacio de memoria
#class Estatica:
#    numero = 1
#    def incrementa():
#        Estatica.numero += 1
#Estatica.incrementa()
#Estatica.incrementa()
#Estatica.incrementa()
#print(Estatica.numero)
#Estatica.incrementa()
#print(Estatica.numero)

#TODO ejemplo herencia
#class Juguete:
#    _encendido = True
#    def apaga(self):
#        self._encendido = False
#    def enciende(self):
#        self._encendido = True
#    def isEncendido(self):
#        return self._encendido

#class Potato(Juguete):
#    def quitarOreja(self):
#        pass
#    def ponerOreja(self):
#        pass   

#class Dino(Juguete):
#    def verEscamas(self):
#        pass

#p = Dino()
#p.enciende()
#print(p.isEncendido())

#TODO constructor en una clase
#class Juguete:
#    _encendido = True
#    def apaga(self):
#        self._encendido = False
#    def enciende(self):
#        self._encendido = True
#    def isEncendido(self):
#        return self._encendido

#class Potato(Juguete):
#    def quitarOreja(self):
#        pass
#    def ponerOreja(self):
#        pass   

#class Dino(Juguete):
#    def __init__(self,nombre):
#        print('hola',nombre)
#    def verEscamas(self):
#        pass

#p = Dino()
#print(dir(p))
#p.enciende()
#print(p.isEncendido())

#TODO CONTRUCTOR EN CLASES

#class Dino:
#    def __init__(self,nombre):
#        print('hola',nombre)
#    def verEscamas(self):
#        pass

#p = Dino('sebas')

#TODO DESTRUCTOR EN CLASES

#class Dino:
#    color = None
#    nombre = None
#    def __init__(self,nombre):
#        self.color = 'verde'
#        self.nombre = nombre
#        print('hola')
#    def verEscamas(self):
#        pass
#    def __del__(self):
#        print('estoy en el destructor dela clase ', self.__class__)

#p = Dino('sebas')
#print(p.color,p.nombre)
#print('el destructor se ejecuta')
#print('despues de terminado el programa')

#TODO DESTRUCTOR EN CLASES
#se puede forzar la ejecucion con del(clase) pero si luego de ello
#vas a utilizar la instancia de la clase el destructor ya la ha destruido :)
# aca un ejemplo 

class Dino:
    color = None
    nombre = None
    def __init__(self,nombre):
        self.color = 'verde'
        self.nombre = nombre
        print('hola')
    def verEscamas(self):
        print('escamas')
    def __del__(self):
        print('estoy en el destructor dela clase ', self.__class__)

p = Dino('sebas')
print(p.color,p.nombre)
print('el destructor se ejecuta')
#del(p)
print('despues de terminado el programa')
p.verEscamas()# si descomentamos la linea 139 esta linea falla por que esta destruida la instancia de la clase


