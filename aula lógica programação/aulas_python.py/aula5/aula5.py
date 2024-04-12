


# Comando FOR

"""
Exemplo 1


    i = int(input("Valor inicial: "))
f = int(input("Valor final: "))
p = int(input("Qual o incremento: "))

if i > f:
    print("O valor final deve ser maio que o inicial: ")
else:
    for x in range(i, f, p):
        print(x, "Bom dia")
"""
'''
Exemplo 2

for x in range(0, 9, 1):
for x in range(9):
        print(x, "Bom dia")
'''

"""
Exemplo 3
    
for x in range(9, 0, -1):
     print(x, "Bom dia")
"""
###############################################

#Comando WHILE

""" 
Exemplo 1
x = 0

while x < 9:   #enquando x menor que 9
    print(x, "Bom dia")
    x = x + 1
    
x = 1

while x <= 9:   #enquando x menor que 9
    print(x, "Bom dia")
    x += 1
"""

"""
x = 1

while True:   #enquando x menor que 9
    print(x, "Bom dia")
    x += 1
    
    if x == 5 or x == 15 or x > 200:
        teclado = input("Continuar s/n?")
        if teclado == "n":
            break    #comando de QUEBRA de loop
"""

##############################################

# Resultado de divisões

# resultado = 7 / 2        # #resultado real

# resultado = 7 % 2        #resultado módulo da divisão. Resto inteiro

# resultado = 7 // 2         #resultado interiro

# print(resultado)