import calculadora

def main():
    operacion = int(input('ingresa un numero para escoger la operacion \n1.suma\n2.resta\n3.multiplicacion\n4.division\n'))
    
    if (operacion == 1):
        num1 = int(input('ingresa primer numero para la suma'))
        num2 = int(input('ingresa segundo numero para la suma'))
        resultado = calculadora.suma(num1,num2)
        print('el resultado de la operacion es ', resultado)

    elif(operacion == 2):
        num1 = int(input('ingresa primer numero para la resta'))
        num2 = int(input('ingresa segundo numero para la resta'))
        resultado = calculadora.resta(num1,num2)
        print('el resultado de la operacion es ', resultado)

    elif(operacion == 3):
        num1 = int(input('ingresa primer numero para la multiplicacion'))
        num2 = int(input('ingresa segundo numero para la multiplicacion'))
        resultado = calculadora.multiplicacion(num1,num2)
        print('el resultado de la operacion es ', resultado)
    elif(operacion == 4):
        num1 = int(input('ingresa primer numero para la division'))
        num2 = int(input('ingresa segundo numero para la division'))
        resultado = calculadora.division(num1,num2)
        print('el resultado de la operacion es ', resultado)
    else:
        print('introduzca un valor correcto')
        
if __name__ == '__main__':
    main()