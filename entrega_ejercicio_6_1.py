class Vehiculo: 
    color = 'roja'
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 80
    cilindraje = 250

c = Coche()
print('color:',c.color)
print('ruedas:',c.ruedas)
print('puertas:',c.puertas)
print('velocidad:',c.velocidad)
print('cilindraje:',c.cilindraje)

