# > mayor
# >= mayor o igual
# == exactamente igual
# < menor
# <= menor o igual
a = 5
b = 6
c = 7


#resultado = (a < b and c <= 7)
#resultado = (a < b && c <= 7)
# resultado = False and False
# resultado = False
#print(resultado)

#tabla de la verdad AND
print("AND")
print("1 1", True and True)
print("1 0", True and False)
print("0 1", False and True)
print("0 0", False and False)

#tabla de la verdad OR
print("OR")
print("1 1", True or True)
print("1 0", True or False)
print("0 1", False or True)
print("0 0", False or False)

#tabla de la verdad XOR
print("XOR")
print("1 1", True ^ True)
print("1 0", True ^ False)
print("0 1", False ^ True)
print("0 0", False ^ False)


a = 5
b = 6
c = 7

resultado = (a >= 5 or c > 7)

print(resultado)
