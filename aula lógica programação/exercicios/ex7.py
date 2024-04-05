""" Exercício 7 """

# Ler 3 números e imprimi-los em ordem crescente.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
        
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
        
if num3 < num1 and num3 < num2:
    if num1 < num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)