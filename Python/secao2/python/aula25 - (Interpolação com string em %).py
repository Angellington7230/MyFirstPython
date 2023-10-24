"""
Interpolação básica de string
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.983942
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('0 hexadecial de %d é %05X' % (15, 15))

# Modos de Fazer: interpolação / f strings / format