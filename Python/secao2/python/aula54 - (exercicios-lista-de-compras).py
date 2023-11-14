'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista.
'''

listar = []
apagar = listar.remove
inserir = listar.append

while True:
    input = 'adicionar(a) / excluir (e) / listar(l) ':
    if 