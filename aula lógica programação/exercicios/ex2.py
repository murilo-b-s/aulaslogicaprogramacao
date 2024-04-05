""" Exercício 2 """

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

