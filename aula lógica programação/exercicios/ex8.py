""" Exercício 8 """

#Faça um algoritmo que leia valores para as variáveis a, b e c e mostre o resultado da seguinte expressão:
#( a – b ) * c

def expressao(a, b, c):
    resolucao = (a - b) * c
    return resolucao

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

print("O resultado da expressão é: ", expressao(a, b, c))