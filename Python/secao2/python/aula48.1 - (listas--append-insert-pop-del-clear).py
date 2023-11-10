"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, + 
Create Read Update   Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)


append(adiciona)
pop(elimina o do meio)
del(elimina)
"""
lista = [10, 20, 30, 40]
print(lista)

numero = lista[2]

# Apagando algum elemento da lista
del lista[3]
print(lista)

print(lista)
print(lista[2])
# Cuidado, pode ficar muito pesado se tiver muita coisa.

# É possível jogar o valor de uma lista em uma variável


# Função append (adiciona na lista)
lista.append(50)
lista.pop()
lista.append(100)
lista.append('Isabela')
lista.append('Yanni')
lista.pop()
print(lista)

