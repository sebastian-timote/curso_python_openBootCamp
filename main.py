
lista = ['hola', 'mensaje', 'adios']

for palabra in lista:
    temporal = False
    if palabra == 'mensaje':
        print('palabra encontrada')
        break
else:
    print('no la he encontrado')

print(temporal)

        


