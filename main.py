#POO
class Dino:
    _encendido = True
    def apaga(self):
        self._encendido = False
    def enciende(self):
        self._encendido = True
    def isEncendido(self):
        return self._encendido

#la instancia d es un espacio de memoria diferente a d2
#por eso tienen resultados diferentes
d = Dino()
d.apaga()
print(d.isEncendido())

d2 = Dino()
d2.enciende()
print(d2.isEncendido())
# por convencion de programadores no deberiamos modificar un metodo o variable cuando tenga guion abajo antes
#self-> podemos modificar el valor de una variable de la clase(global) ya que si no lo ponemos creamos una nueva variable con el mismo nombre del ambito del metodo




