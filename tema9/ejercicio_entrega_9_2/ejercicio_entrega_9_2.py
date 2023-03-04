# teneis que crear una aplicacion que obtendra los elementos impares de una lista pasada
# por parametro con filter y realizara una suma de todos estos elementos obtenidos
# mediante reduce
from functools import reduce
listaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def impares(x):
    if x % 2 == 0:
        return False
    return True

listaImpares = filter(impares,listaNumeros)
sumaImpares = reduce(lambda a,b: a + b, listaImpares)
print(sumaImpares)
