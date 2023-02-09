
#sys.path es una variable que almacena rutas de modulos
import sys
#en esta linea agregamos una nueva ruta ala variable path para que
# busque alli modulos que vamos a crear en este caso el modulo saluda.py
sys.path.append('/home/unfulanoubuntu/archivos_test/python/mismodulos')
import pprint
pprint.pprint(sys.path)
import saluda
def main():
    saluda.saluda('sebas')

if __name__ == '__main__':
    main()