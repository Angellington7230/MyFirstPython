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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)