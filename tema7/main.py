# team ambitos

import operaciones2.sumador.suma as s
import pprint

def test():
    print('hola')

numero = 4
obj = s.suma(2,2)
#podemos ver todos las variables y funciones en el ambito global
pprint.pprint(globals())
