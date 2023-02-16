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

#class Juguete:
#    nombre = ""
#    precio = 0.0
#    def __init__(self, nombre , precio):
#        self.nombre = nombre
#        self.precio = precio
    
#    def __str__(self):
#        return f'Mi nombre es {self.nombre} y mi precio {self.precio}' 

    
#j1 = Juguete("potato",200)
#j2 = Juguete("dino",3.4)

#print(j1)
#print(repr(j2))

# TODO EJEMPLO para ver todos los metodos de una cadena
#import pprint
#pprint.pprint(dir(''))
# TODO metodos de una cadena
#cadena = "      en un lugar de la manchA          "
#print(cadena.title())# coloca las letras iniciales de cada palabra en mayus
#print(cadena.capitalize())# coloca la primera letra en mayus
#print(cadena.lower().count('a'))#pasar a minus y cuantas veces se repite una letra
#print(cadena.strip())#quita los espacios iniciales
#print(cadena.lstrip())#quita los espacios a la izquierda
#print(cadena.rstrip())#quita los espacios a la derecha
cadena2 = 'hola otravez mama bitch'
print(cadena2.split(' '))
print(cadena2.startswith('ho'))
print(cadena2.endswith('ch'))


#isdigit solo funciona con cadenas con int casca
#numero = '5'
#print(numero.isdigit())# comprueba si es string
#numero = 'a'
#print(numero.isalnum()) # comprueba si es alfanumerico
#print(numero.isalpha()) # comprueba si es letras





        
        



