'''
split e join com list e str
split - divide uma string
join - une uma string
'''

        # split
frase = 'Secsu com Ivana Forte Chaves'
lista_frases_cruas = frase.split(',')


        # strip - corta espaços entre o  começo e o fim do string
# lstrip -> LeftStrip ... Corta o espaço da esquerda
# rstruo -> RightStrip ... Corta o espaço da direita

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases,)

frases_unidads = ''.join('abc')