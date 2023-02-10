# tema ambitos
import pprint
variable= 5
print(variable)
#cambiando el valor de la variable usando el dicc. globals
globals()['variable'] = 6
print(variable)

def prueba():
    valor =5
    estado = False
    pprint.pprint(locals())

prueba()



