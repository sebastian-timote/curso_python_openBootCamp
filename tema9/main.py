# BIBLIOTECA STANDARD DE PYTHON Y FUNCIONES BUILT IN
# TODO programacion multihilos
# hay que darle tiempo para que se ejecuten los hilos
# por que si el programa principal se ejecuta muy rapido no se alcanzan a ejecutar los hilos
# se ejcuta el primer hilo y sigue con el segundo sin esperar a terminar el primer hilo
#import _thread
#import time

#def horaActual(nombreThread,tiempoEspera):
#    count = 0
#    while count < 5:
#        time.sleep(tiempoEspera)
#        count += 1
#        print(f'hilo: {nombreThread} - {time.ctime(time.time())}')

#_thread.start_new_thread(horaActual, ('thread_uno',1))
#_thread.start_new_thread(horaActual, ('thread_dos',2))
#print('he disparado ya los hilos')
#while True:
#    pass

# TODO paquete logging
#import logging
#sirve para mostrar los mensajes de info en consola
# EXISTEN NIVELES DE AVISOS
#DEBUG -> NIVEL 1
# INFO ->NIVEL 2
# WARNING -> NIVEL 3
# ERROR -> NIVEL 4
# CRITICAL -> NIVEL 5
#(level=logging.WARNING)-> SOLO MUESTRA DEL NIVEL 3 Y NIVEL 4 Y NIVEL 5

#logging.basicConfig(level=logging.DEBUG)
#logging.debug('prueba debug')
#logging.info('Arrancando programa')
#logging.warning('hace calor!!')
#logging.error('test')
#logging.critical('adios')

#TODO BIBLIOTECA STANDARD FUNCIONES BUILT IN
# MAP FILTER REDUCE
#TODO FUNCION FILTER
# filter(funcion,lista)
# la funcion debe estar ya definida o ser una lambda y 
# debe retornar true o false
# si filter recibe un true devuelve el resultado y lo pone en una lista
# si recibe un false quita el resultado
#numeros = [1,2,3,4,5,6,7,8,9,10]
#def miFuncion(x):
#    if x % 2 == 0:
#        return True
#    return False
#resultado = filter(miFuncion, numeros)
# como devuelve lista toca imprimirlo con la funcion list()
#print(list(resultado))

# TODO otro ejemplo de filter
#def miFuncion(x):
#    if str(x).startswith('pep'):
#        return True
#    return False
#resultado = filter(miFuncion, ['pepe','pepito','juan'])
#print(list(resultado))

# TODO FUNCION MAP
# map aplica una funcion a todos los elementos de un alista o tupla
# a elementos iterables
# map(funcion, lista)

##resultado = map(lambda x: x*x , [1,2,3,4,5,6,7,8,9])
#print(list(resultado))

# TODO funcion reduce
#reduce(funcion,lista)

#from functools import reduce
#def suma(a,b):
#    return a + b
#res = reduce(suma, [1,2,3,4,5]) 
#print(res)

#TODO FUNCION ZIP
# asocia valores de dos listas

#cursos = ['java','python','git']
#asistentes = [15,20,4]
#demo = zip(cursos,asistentes)
#print(list(demo))

#TODO FUNCIONES ALL() Y ANY()
#ALL() VERIFICA QUE TODAS LAS CONDICIONES DE LA LISTA SE CUMPLAN
#ANY() VERIFICA QUE AL MENOS UNA DE LAS CONDICIONES DE LA LISTA SE CUMPLAN

#listaA = [ 1 == 1,2 == 2,3 == 3]
#res = any(listaA)
#res2 = all(listaA)
#print(res)
#print(res2)

#TODO FUNCION ROUND()
# redondea un float al valor mas cercano
#a = 5.5
#b = 5.6
#c = 5.4
#print(round(a))
#print(round(b))
#print(round(c))

# TODO MIN()
# ME DEVUELVE EL VALOR MINIMO DE UNA LISTA
#print(min(2,3,4,5,6,4,1))

# TODO pow()
# elevar un numero ala potencia
#print(pow(2,4))
#print(2**4)

# TODO sorted()
#ordenar unalista

#lista = ['z','c','d','a']
#ordenada = sorted(lista, reverse=True, key=lambda x: str(x).startswith('a'))
#print(ordenada)

# TODO funcion input()
# permite preguntar al usuario por un dato
# TODO FUNCION GETPASS
# OBTIENE UNA CONTRASEÑA Y EN CONSOLA NO APARECEN LOS DIGITOS INTRODUCIDOS POR SEGURIDAD
#from getpass import getpass
#user  = input('username: ')
#passwd  = getpass('password: ')
#print(user, passwd)

secreto = 50
valor = 0
while valor != secreto:
    valor = int(input('introduce un numero: '))
    if valor > secreto:
        print('valor muy alto')
        continue
    if valor < secreto:
        print('valor muy bajo')
        continue
    print('acertaste')










