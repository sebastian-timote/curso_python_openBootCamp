
#def miFuncion(nombre):
#    print('hola', nombre)
#def suma(a, b):
#    print(a + b)     

#miFuncion('victor')
#suma(5,4)

#FUNCIONES DENTRO DE FUNCIONES
#def matematicas(a,b):
#    def suma(a,b):
#       print(a + b)
#    def resta(a,b):
#       print(a - b)
#    def masoperaciones(a,b):
#        def multiplica(a,b):
#            print(a*b)
#        multiplica(a,b)    
#    suma(a,b)
#    resta(a,b)
#    masoperaciones(a,b)
#matematicas(5,3)

#TODO EJEMPLO de alcance de las variables en una funcion
#los parametros y las variables dentor de las funciones solo se pueden acceder desde ella
#variable SHADOWING -> cuando se usa una variable con el mismo nombre y en diferentes scopes
#hoyHace = 12.0
#def miFuncion(nombre):
#    global hoyHace
#    hoyHace = 6.0
#    print('hola,', nombre, 'la temperatura es de ', hoyHace)
#miFuncion('sebas')
#print(hoyHace)
# cuando usamos la palabra reservada global editamos el valor de la variable global

#PARAMETRO OPCIONALES EN UNA FUNCION
#def miFuncion(nombre='juan'):
#    print('hola', nombre)

#miFuncion()
#miFuncion('sebas')
# cuando no se le pasa ningun parametro toma por defecto el que tiene def en la funcion

#def suma(a=1,b=5,c=1):
#    print(a + b + c)
#suma(1,1,1)
#suma(c = 7,b=7,a=7)
#suma(c=7)

#PARAMETROS VARIABLES EN UNA FUNCION

#def suma(*args):
#    resultado = 0
#    for arg in args:
#        resultado += arg
#    print(resultado)
#suma(5,5,5,5,5,5,5,5,5,5)
#suma(2,2)

#PARAMETROS CON NOMBRES(NAMED PARAMETERS) EN UNA FUNCION

#def suma(**kwargs):
#    print(kwargs)
#suma(vivienda= 'dos pisos', coche='ferrari')

#EJEMPLO RECORRIENDO UN DICCIONARIO EN UNA FUNCION CON PARAMETROS VARIABLES
#def suma(**kwargs):
#    for key, value in kwargs.items():
#        print(key, '=', value)
#suma(vivienda= 'dos pisos', coche='ferrari')

#def suma(**kwargs):
#    if kwargs['coche'] == 'bonito':
#        print('tu coche es bonito')
#suma(vivienda= '2 pisos', coche='bonito')

# otro ejemplo verificando que ecista coche para que no casque
def suma(**kwargs):
    if 'coche' in kwargs and kwargs['coche'] == 'bonito':
        print('tu coche es bonito')
suma()





