""" Exercício 11 """

#Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus  Centígrados.

# (Fahrenheit – 32) x 5

#Fórmula: Centígrados = ----------------------------

9

def temperatura(temp):
    conversao = ((temp - 32) * 5) / 9
    return conversao

temp = int(input("Digite a temperatura em Fahrenheit que deseja converter: "))

print("A temperatura em graus Centígrados é: ", temperatura(temp))