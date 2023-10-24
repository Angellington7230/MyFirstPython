# Operadores in e not in / entre - não entre
# String são iteráveis
# 0 1 2 3 4 5 
# O t á v i o
#-6-5-4-3-2-1




nome = 'Otávio'


# print(nome[-5])
# print('á' in nome) # Vai verificar na var se há a letra 'á', e sim e vai retornar para True.

# print('z' in nome) # Vai verificar se tem o 'z', e como não tem, vai retornar para falso.

# print('vio' in nome) # Vai verificar se a sequência tem, e como tem, vai retornar para True.

# print('zero' in nome) # Vai verificar se tem, e como não tem, vai retornar False.
# print(10* '-')
# print('Abaixo serão aqueles que estão em "not in"')

# print('zero' not in nome) # Como não tem, vai verificar como verdadeira.
# print('vio' not in nome) # Como tem, vai relatar como falsa

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em em {nome} ')
else:
    print(f'{encontrar} não está em {nome}')