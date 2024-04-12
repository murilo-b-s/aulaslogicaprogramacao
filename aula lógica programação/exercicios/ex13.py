""" Exercício 13 """

#Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:
#se n <= 10 imprima MENSAGEM 1,
#se n > 10 e <= 100 imprima MENSAGEM 2
#se n >100 imprima MENSAGEM 3,

mensagem1 = "seu número é menor ou igual a 10"
mensagem2 = "seu número está entre 10 e 101"
mensagem3 = "Seu número é maior que 100"

n = int(input("Digite um número: "))

if n <= 10:
    print(mensagem1)
elif n > 10 and n <= 100:
    print(mensagem2)
else:
    print(mensagem3)