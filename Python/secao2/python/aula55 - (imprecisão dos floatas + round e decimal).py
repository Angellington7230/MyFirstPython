'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
'''

# Round arredonda o número
# decimal.Decimal transmite o decimal completo

import decimal

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(type(round(numero_3, 3)))
print(round(numero_3, 3))