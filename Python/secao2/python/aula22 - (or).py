# Operadores Lógicos
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser
# verdadeiras.

# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor falso
# São consideradas falsy (já vimos)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input("[E]ntrar [S]air: ")
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

#             # Referencia com uma única
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Aqui é verificado a propriedade da falsy
# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
