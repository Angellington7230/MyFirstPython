'''Este será um código que a máquina vai perguntar os seus dados e então irá exibi-los!'''


nome = str(input("Digite seu nome: "))
sexo = str(input('Qual é o seu sexo? '))
if sexo == 'M' or 'm' or 'Menino' or 'menino':
    print('Seu machosta')
elif sexo == 'F' or 'f' or 'Menina' or 'menina':
    print('tchu')
else:
    print('Você é colorido!')

while True:
    try:
        dianas = input('Digite o dia do seu nascimento: ')
        if len(dianas) < 2:
            print()
        int_dianas = int(dianas)
    except:
        print('Digite um número coerente!!')
        continue
    break
print(f'Seu nome é {nome}')
print(f'Seu sexo é hehehehehe {nome}, orgulhe-se')
print(f'Dia de nascimento: {int_dianas}')