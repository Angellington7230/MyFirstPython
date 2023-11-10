"""
for in com listas
0 Yanni
1 Ivana
2 Isabela
"""
lista = ['Yanni', 'Ivana', 'Sabrina']
lista.append('Wellington')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])