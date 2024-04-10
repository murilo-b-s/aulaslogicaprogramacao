""" Exercício 9 """

#Faça um algoritmo que mostre o resultado da expressão abaixo:
#(( x – 5) * y) – z
#Obs: Ler valores para as variáveis x, y e z.

def expressao(x, y, z):
    resolucao = ((x - 5)* y) - z
    return resolucao

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

print("O resultado da espressão é: ", expressao(x, y, z))