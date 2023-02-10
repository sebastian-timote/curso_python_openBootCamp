
#import operaciones2.suma

#forma 1 import paquetes 
#import operaciones2.restador.resta
#import operaciones2.sumador.suma

#forma 2 import paquetes forma corta
#import operaciones2.restador.resta as r
#import operaciones2.sumador.suma as s

#forma 3 import de paquetes
#from operaciones2 import restador,sumador

#forma 4 import de paquetes pero necesita config en archivo __init__
#from operaciones2 import *
import operaciones2.restador.resta
import pprint

def main():
    #TODO EJEMPLO 1 PAQUETES
    #print(operaciones2.suma.suma(2,2))

    #TODO EJEMPLO 2 PAQUETES CON CLASE DENTRO DEL MODULO
    #mp = operaciones2.suma.Multiplicador()
    #print(mp.multiplica(5,5))

    #TODO EJEMPLO 3 PAQUETES CONTENIENDO PAQUETES
    #forma2 import
    #print(s.suma(2,2))
    #print(r.resta(2,2))
    #forma 3 import
    #print(sumador.suma(2,2))
    #print(restador.resta(2,2))
    # forma 4
    #print(restador.resta.resta(2,2))
    #TODO VER FUNCIONES O METODOS DE UN OBJETO INT STRING ETC
    pprint.pprint(dir(1))


if __name__ == '__main__':
    main()