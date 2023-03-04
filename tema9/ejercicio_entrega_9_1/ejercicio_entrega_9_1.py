#crea un script que pida al usuario una lista de paises (separado por comas)
# estos se deben almacenar en una lista. no deberia haber paises repetidos
#(haz uso de set).finalmente, muestra por consola la lista de paises ordenados alfabeticamente
# y separados por comas.
import pprint
paises = input('ingresa una lista de paises separadas por coma')
listaPaises = paises.split(',')
conjuntoPaises = set(listaPaises)
ordenarPaises = sorted(conjuntoPaises)
for key in ordenarPaises:
    print(key,',')
 