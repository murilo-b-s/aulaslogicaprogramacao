"""
Exercício 1
#Ler dois números e imprimir as variáveis na mesma ordem que 
# foram digitadas
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("Você digitou os números: \nNúmero 1:",num1, "Número 2:", num2)
"""

"""
# Exercício 2
# Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas
# variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o
# conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.

vA = int( input("Primeiro número: ") )
vB = int( input("Segundo número: ") )
print("Antes da Troca: vA=",vA, "vB==", vB)
# vA = vB   # isto está errado
# vB = vA

vA, vB = vB, vA   # isto está correto
# aux = vA     # isto também está correto
# vA = vB
# vB = aux
print("Após a Troca: vA=",vA, "vB==", vB)
"""
'''
"""
Ler dois valores numéricos e escrever a soma destes.
"""
def soma_dois_numeros(a, b):
    soma = a + b
    return soma
n1 = int( input("Primeiro número: ") )
n2 = int( input("Segundo número: ") )
print("Soma=", soma_dois_numeros(n1, n2))
'''
'''
# Explicando o COMANDO if elif else
n = 15
# if n == 10:  # ==   !=   >=   <= 
#     print("Este é o número 10")
# else:
#     print("Este número não é o 10")
#     if n > 10:
#         print("Número é maior que 10")
#     else:
#         print("Númeor é menor que 10")

if n == 10:  # ==   !=   >=   <= 
    print("Este é o número 10")
elif n > 10:
        print("Número é maior que 10")
else:
        print("Númeor é menor que 10")
'''

'''
Exercício 4

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

def soma_cinco(a, b, c, d, e):
    soma = a + b + c + d + e
    return soma

num1 = int( input('Digite o primeiro número: '))
num2 = int( input('Digite o segundo número: '))
num3 = int( input('Digite o terceiro número: '))
num4 = int( input('Digite o quarto número: '))
num5 = int( input('Digite o cinco número: '))

soma = num1 + num2 + num3 + num4 + num5

print('A soma dos valores é: ', soma_cinco(num1, num2, num3, num4, num5))
print('A média dos valores é: ', (soma / 5))
'''
