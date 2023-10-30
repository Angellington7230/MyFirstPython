"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    print(1)
    print(2)
    print(3)
    break

while condicao:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print("Acabou a repetição!")