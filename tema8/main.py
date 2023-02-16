#formateo de cadenas
#numero = 511
#texto = "quijote"
#otromas = 1.2
#TODO forma 1 antes de python 2.6 se hacia de esta manera

#print("el numero es %d y el texto es %s y tiene %.2f" % (numero,texto,otromas))

#TODO forma 2 despues de python 2.6 se empezo a utilizar esta forma
# y se dejo de utilizar hasta la version 3.6

#print("el numero es {} y el texto es {} y tiene {}".format(numero,texto,otromas))
#diferentes formas indicando el orden como si fuera un array
#print("el numero es {1} y el texto es {0} y tiene {2}".format(texto,numero,otromas))
# o puede ser tambien con parametros nombrados
#print("el numero es {n1} y el texto es {t1} y tiene {f1}".format(n1=numero,t1=texto,f1=otromas))

#TODO forma 3 despues de python 3.6 se empezo a utilizar esta forma las fstrings cadenas tipo f
# no es muy utiliza por desconocimiento
# ademas que se puede invocar metodos de python
#def suma(a,b):
#    return a + b 
#print(f'el numero es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}')

# TODO uso de str() y de repr()
# los dos metodos convierten de algo a string
#str() -> se utiliza para una salida informal para el usuario
#repr() -> se utiliza para generar salidas de depuracion y desarrollo

#print(type(numero))
#numerotxt = str(numero)
#print(type(numerotxt))

#numerotxt2 = repr(numero)
#print(type(numerotxt2))

# TODO otro ejemplo de str() y repr()

class Juguete:
    nombre = ""
    precio = 0.0
    def __init__(self, nombre , precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio {self.precio}' 

    
j1 = Juguete("potato",200)
j2 = Juguete("dino",3.4)

print(j1)
print(repr(j2))

        
        



