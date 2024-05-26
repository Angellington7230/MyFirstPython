# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outros
# tipos imutáveis e primitivos
# str, int, float, bool

print(1) # output: 1
print("1", type("1")) # output: 1 <class 'str'>

print(int('1'), type(int('1'))) # output: 1 <class 'int'>
print(str(1) + 'b') # output: 1b

print(float(1)) # output: 1.0

print(bool('')) # output: False
print(bool(" ")) # output: True 