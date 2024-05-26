# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressao

# Poderá armazenar qualquer coisa
nome = 'Minerva Alves Barbosa'
idade = 18
maior_de_idade = 18

dois_mais_dois = 2 + 2
print(dois_mais_dois) # output: 4

print(f'{nome} tem a idade de {idade} anos.') # output: Minerva Alves Barbosa tem a idade de 18.
print(f'Maioridade é {maior_de_idade >= idade}') # output: Maioridade é True

tipo = type(int('1')) 
print(tipo) # output: <class 'int'>
