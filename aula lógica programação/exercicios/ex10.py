""" Exercício 10 """

#Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
#(nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
#Cálculo da Média Ponderada = ------------------------------------------------------------------------
#soma dos pesos

def media(nota1, nota2, peso1, peso2):
    resultado = ((nota1 * peso1)+ (nota2 * peso2)) / (peso1+ peso2)
    return resultado

nota1 = int(input("Digite a primeira nota: "))
peso1 = int(input("Digite o peso da primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
peso2 = int(input("Digite o peso da segunda nota: "))

print("A media ponderada é:", media(nota1, nota2, peso1, peso2))