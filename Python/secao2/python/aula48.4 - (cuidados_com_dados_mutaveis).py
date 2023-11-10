"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Isabela'
# outra_var = nome
# nome = 'Yanni'
# print(nome)
# print(outra_var)


lista_a = ['Isabela', 'Yanni']
lista_b = lista_a.copy()

lista_a[1] = 'Não é boneca'
print(lista_a)
print(lista_b)
