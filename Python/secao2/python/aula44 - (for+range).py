'''
For + range
range -> range(start, stop, step)
'''
numeros = range(10)
numeros2 = range(5, 10)
numeros3 = range(5, 10, 2)

print(numeros)
print(numeros2)
print(numeros3)

for numero in numeros3:
    print(numero)

# Numeros pares de 0 a 100

par = range(0, 100, 2)

for pari in par:
    print(pari)