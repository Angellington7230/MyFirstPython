nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número ') # Conversão em uma linha - Mas da pra fazer a checagem depois
numero_2 = input('Digite outro número: ')

# Conversão... Isso é bom para lembrar do primeiro valor digitado e não gera um erro no código

#Evita concatenaçaõ
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')