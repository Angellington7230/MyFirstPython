'''
Introdução ao desempacotamento + tuples (tuplas)
'''


# Cuidado para não mais ou menos valores que a variável

__, __, nome1, *__ = ['Isabela', 'Yanni', 'Ivana']
print(nome1, __)

# O ASTERISCO É O RESTO!

# o '__' = Variável que tá ali, mas não vou usar ela.