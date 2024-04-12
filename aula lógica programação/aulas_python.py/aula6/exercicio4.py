
""" Altere o exercício anterior para que a digitação dos números aceite somente números positivos. """

i = 0
while i < 3:
    
    num1 = 0
    while num1 <= 0:
        num1 = int(input("Digite o primeiro número: "))
        if num1 < 0:
            print("Número inválido. Digite um número positivo.")                #     Primeira forma

    while True:
        num2 = int(input("Digite o segundo número: "))
        if num2 < 0:
            print("Número inválido. Digite um número positivo.")                #     Segunda forma
        else: 
            break
    
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

