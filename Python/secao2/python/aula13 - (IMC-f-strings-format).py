nome = 'Isabela'
altura = 1.63
peso = 45
imc = peso / (altura * altura) # IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura:.4f} de altura' #Esse "4f"refere a quantidade de casas decimais no valor numérico.
linha_2 = f'{nome} possui {imc:.2f} de imc)'
print(linha_1)
print(linha_2)

#f significa format!!