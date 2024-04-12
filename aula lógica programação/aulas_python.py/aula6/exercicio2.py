
""" Faça o exercício anterior repetir 3 vezes. """

i = 0
while i < 3:
    num1 = int(input("Digite o primeiro número: "))
    if num1 < 0:
        num1 = int(input("Digite um número positivo: "))
    num2 = int(input("Digite o segundo número: "))
    if num2 < 0:
        num2 = int(input("Digite um número positivo: "))
    

    if (num1 - num2) == 1 or (num1 - num2) == -1:
        print("Não há números inteiros entre esses números.")

    if num1 < num2:
        for x in range(num1, num2 -1, 1):
            x += 1
            print(x)
            
    elif num1 == num2:
        print("Esses números são iguais.")
        
    else:
        for x in range(num1, num2 +1, -1):
            x -= 1
            print(x)
#        print(x, end=" ")    # Deixa o print no terminal em linha    ex: 6 5 4

    i += 1
