"""
enumarate - enumerara iteráveis (índices)
"""
lista = ['Yanni', 'Ivana', 'Sabrina']
lista.append('Wellington')

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# Mesma coisa

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
    # Muito mais gostoso!!

# Indo para índice

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')