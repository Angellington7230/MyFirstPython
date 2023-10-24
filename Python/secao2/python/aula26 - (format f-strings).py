"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= -  Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.:0>-100, 1f
Conversion flags - !r !s !a  __
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}') # Preenche até completar 10 caracteres na direita
print(f'{variavel: <10}.') # Preenche até completar 10 caracteres na esquerda
print(f'{variavel: ^10}') # Até chegar no centro (ou tentar)
print(f'{variavel:-^10}') # Pode ser preenchido
print(f'{100.204242424252:0=+10,.1f}') # Dá pra separar por vírgula, definir o sinal sim ou não... Felizmente existem bibliotecas.

print(f'P hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}') # O "r" é outro método