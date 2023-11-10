"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, +
"""
#       01234
#       54321


# string = 'ABCDE' # 5 caracteres
# lista = []
# lista2 = list()
# print(lista, type(lista))
# print(lista2, type(lista2))
# # Se a lista estiver vazia, ela é False
# print(bool(lista))

#         0     1           2             3   4
#         -5    -4          -3            -2  -1
lista = [123, True, 'Isabela Aloe Vera', 1.2, []]
print(lista)

#reatribuindo valor
lista[2] = 'Wellington Ferreira'
print(lista)
print(lista[2], type(lista[2]))