# Função print()
print("Hello World") # output: Hello World

print(7) # output 7
print(12, 64) # output: 12 64
print(12, 64, sep=" ") # output: 12 64
print(12, 64, sep="-") # output: 12-64
print("Hoje é dia", "de Minerva", sep=" => ") # output: Hoje é dia => de Minerva

# sep => separador de métodos e argumentos

print("Nossa vida", "tanto falta", end='\n') # padrão
#output: Nossa vida tanto falta

# end => final da linha

print("Phony", end='-') # output: Phony-Anya Forger (emenda com a próxima)

print("Anya Forger", sep=" ", end="\n\r") #output: Phony-Anya Forger

#\r\n - CRLF - Windows (Fim de linha e ir para a próxima)
#\n - LF - Unix (Fim de Linha)