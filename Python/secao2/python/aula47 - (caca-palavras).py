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

import os


palavra_secreta = 'Sopa'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    print('Palavra formada: ', palavra_formada )

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!!')
        print('A palavra era', palavra_secreta)
        print('Tentativas', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0