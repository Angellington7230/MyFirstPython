"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

'''
Tem que ter uma variavel entrada
alguma coisa vai verificar a variavel entrada pra ver se tem a letra
se tiver a letra, vai adicionar no alfabeto e vou ter que continuar a escrever

Quando estiver completo, vão me agradecer!!!
'''





# A Palavra será Isabela



palavra = 'Isabela'
print(palavra[0])

while True:
    entrada = input('Qual é a palavra secreta? ')
    if entrada == ('i') or ('I'):
        print('Está na palavra! ')
    else:
        print('Não está na palavra!')