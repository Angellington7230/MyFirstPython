"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

# As ids são o espaço ocupado na memoória


v1 = 'a'
print(id(v1))

a = '3'
print(id(a))


# Vamos fazer a verificação:
print(id(a) == id(v1))          #Vai dar falso, pois é mentira, eles não ocupam o mesmo espaço na memória.
