"""
Fatiamento de string
012345678
Olá mundo
-987654321
Fatiamento [1:f:p] [::] - ([iníci:final:passo])
Obs.: a função len retorna a qtd
de caracteres da str
"""

# Fatiamento
variavel = 'Satoru Gojo'
print(variavel[0:6]) # Foi de Satoru Gojo

print(len(variavel[0:6:])) # Foi de Satoru Gojo - Vai printar a quantidade de caracteres de Satoru... Ou seja... 6

print(variavel[-1:-10:-1]) # Inverteu a string - Passou negativo vai para trás