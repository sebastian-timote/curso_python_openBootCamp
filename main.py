# > mayor
# >= mayor o igual
# == exactamente igual
# < menor
# <= menor o igual
# a = 5
# b = 6
# c = 7


#resultado = (a < b and c <= 7)
#resultado = (a < b && c <= 7)
# resultado = False and False
# resultado = False
#print(resultado)

#tabla de la verdad AND
#print("AND")
#print("1 1", True and True)
#print("1 0", True and False)
#print("0 1", False and True)
#print("0 0", False and False)

#tabla de la verdad OR
#print("OR")
#print("1 1", True or True)
#print("1 0", True or False)
#print("0 1", False or True)
#print("0 0", False or False)

#tabla de la verdad XOR
#print("XOR")
#print("1 1", True ^ True)
#print("1 0", True ^ False)
#print("0 1", False ^ True)
#print("0 0", False ^ False)


#a = 5
#b = 6
#c = 7

#resultado = (a >= 5 or c > 7)

#print(resultado)
#contador = 1
#while contador <= 10:
#    if contador % 2 == 0:
#        print(contador, 'es un numero par')
#    contador += 1

# EJEMPLO BREAK
#contador = 1
#while contador <= 10:
#    if contador == 5:
#        print('rompo el ciclo')
#        break #break detiene ejecucion de while
#    print('contador vale ',contador)
#    contador += 1
#print('fuera while')

# EJEMPLO continue
#contador = 1
#while contador <= 10:
#    if contador % 2 == 0:
#        print(contador, 'es un numero par')
#        continue
#    print('y ahora incremento el contador')
#    contador += 1
#print('fuera while')

#BUCLE FOR

#lista = [1,2,3,'a',5]
#tupla = (1,2,3,'c','d')
#for valorActual in tupla:
#    print(valorActual)

#longitud = len(lista)
#print(longitud)

#for numero in range(len(lista)):
#    print(lista[numero])

#lista = ['hola','mensaje','adios']
#for palabra in lista:
#    print('palabra actual: ',palabra)
#    if palabra == 'mensaje':
#        print('he encontrado la palabra mensaje')
#        break

#OTRA FORMA con IN 

#if 'mensaje' in lista:
#    print('éncontre palabra mensaje')

#forma con NOT IN

#if 'mensaje' not in lista:
#    print('éncontre palabra mensaje')

#lista = [3,4,1,2,5]
#print(lista)
#listaOrdenada = sorted(lista)#ordena la lista consecutivamente
#listaOrdenada = sorted(lista, reverse=True)#la ordena pero en reversa
#print(listaOrdenada)
#lista = ['A','a','p','P','Z','z']
#print(lista)
#listaOrdenada = sorted(lista)
#print(listaOrdenada)#lo ordena en el orden del formato ASCCI

#valor = 3

#if valor ==1:
#    print('valor es 1')
#elif valor ==2:
#    print('valor es 2')
#elif valor ==3:
#    print('valor es 3')
#elif valor ==4: 
#    print('valor es 4')
#elif valor ==5:
#    print('valor es 5')

#forma de hacer un switch apartir de la version python 3.10
#no funciono el switch en python 3.10 :'(
#valor = 4

#match 4:
#    case 1:
#        print('valor es 1')
#    case 2:
#        print('valor es 2')
#    case 3:
#        print('valor es 3')
#    case 4:
#        print('valor es 4')
#    case 5:
#        print('valor es 5')

        


