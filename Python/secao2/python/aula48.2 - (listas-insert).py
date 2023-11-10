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
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

"""
#         0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Isabela')
nome = lista.pop()
# lista.clear()             Elimina a lista toda!
lista.insert(0, 'Isabela')
print(lista)