# Aprendendo para vencer!!

import time

# # Utilizando a técnica do Try Catch *1*
# while True:
#     try:
#         numero = input('Insira um número: ')
#         numero_int = int(numero)
#         break
#     except: 
#         print('Insira um número de verdad!! ')
#     continue
# print(f'O número informado foi {numero_int}!!')


# # Utilizando algo mais simples. If e else!! *2*
# while True:
#     numero = input('Insira um número: ')

#     if numero.isdigit():
#         numero_int = int(numero)
#         print(f'O seu número é {numero_int}')
#         break
#     else:
#         print('Insira um número de verdade!')


    


# # Número da namorada!!





while True:
    namorada = input("Insira o nome da namorada: ")

    if len(namorada) > 0:
        break
    else:
        print('Digite alguma coisa!')
        print('---------------------------------')
        continue
print('---------------------------------')
while True:
    ninicial = input('A sua namorada é de que país? ')

    if ninicial == 'Brasil' and 'brasil':
        ninicial = '+55'
        print('---------------------------------')
        break
    else:
        print("Ela nem existe kkkk")
        print('---------------------------------')
        continue
    
#up
while True:
    DD = input('De onde é sua namorada? ')
    # if DD == 'Rio Grande do Sul' and 'RS':
    #     DD = '81'
    #     break
    # elif DD == 'Ceará' and 'CE':
    #     DD = '85'
    #     break
    # else:
    #     print('Digite um DD correto')
    #     continue


while True:
    numero_namorada = input('Insira o número da namorada')
    if len(numero_namorada) == 9:
        break
    else:
        print('Digite a quantidade correta')
        continue



    #estrutura de um número -> +55 DD 98147-5212

print(f'{ninicial} {DD} 9 {numero_namorada[0:8:4]}')

print('Eu sei o nome da sua namorada!')
time.sleep(3)
print(f'O nome da sua namorada é {namorada},', end='', flush=True)
time.sleep(2)
print(' e o numero dela é (insira numero aqui)')

