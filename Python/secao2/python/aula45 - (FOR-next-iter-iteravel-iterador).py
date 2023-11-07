'''
Iterável - > str, range, etc (que possuem o método __iter__)
Iterador -> quem sabe entregar um valor por ver
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

# texto = 'Luiz'
# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)

# texto = iter('Luiz') #__iter__()
# print(texto)

# print(texto.__next__())   #chama o próximo valor
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# print(next(texto))          #outro modo de dar next
# print(next(texto))
# print(next(texto))
# print(next(texto))




# for letra in texto (é o que acontece)
texto = 'Angel' # iterável (um string)
iterador = iter(texto) # iterador 

while True:
    try:
        letra = (next(iterador))
        print(letra)
    except StopIteration:
        break




