#funcion que diga si un año (numero entero)es bisiesto o no
ano = int(input('escribe un año que quieras saber si es bisiesto '))

def saberAnoBisiesto(valor):
    if (valor % 4 == 0):
        if (valor % 100 != 0):
            return ' es un año bisiesto'
        elif(valor % 400 == 0):
            return ' es un año bisiesto'
        else:
            return ' no es un año bisiesto'
    else:
        return ' no es un año bisiesto'

resultado = saberAnoBisiesto(ano)
print('el año ',ano, resultado)
