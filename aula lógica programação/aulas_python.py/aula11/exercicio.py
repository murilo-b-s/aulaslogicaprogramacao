"""
Para o exercício considere as seguintes listas: 
listaA, listaB, listaC
Você tem um código funcional mas parcial que mostra
um menu com várias opções. 
Você deverá finalizar o código implementando 
as opções que faltam.
"""

menu = """
    ========================================
    1- Adicionar um elemento na listaA
    2- Retirar um elemento na listaA
    3- Digite um elemento e mostre sua posição 
        na listaA
    4- Digite uma posição e diga qual o elemento 
        ocupa essa posição na listaA
    5- Copie todos os números para pares da 
        listaA para a listaB
    6- Copie da listaA para a listaC todos os 
        números que tiverem apenas 2 dígitos
    7- Imprima todas as listas mostrando o 
        nome da lista, seus elementos e suas posições.
    8- Finaliza o código
    ========================================    """

listaA = []
listaB = []
listaC = []
lista_numeros = []

listaA = ['6', '4', '5', '89', '4', '35']
while True:
    print(menu)
    escolha = input("Escolha: ")
    if escolha == '1':
        elemento = input("Digite o que deseja adicionar à lista A: ")
        listaA.append(elemento)
        print(listaA)
        continue

    if escolha == '2':
        elemento = input("Digite o que deseja retirar da lista A: ")
        if elemento in listaA:
            listaA.remove(elemento)
            print(listaA)
        else: 
            print("Elemento não encontrado!")
        continue

    if escolha == '3':
        elemento = input("Digite um elemento: ")
        if elemento in listaA:
            posicao = listaA.index(elemento)
            print(posicao)
        else:
            print("Elemento não encontrado!")
        continue

    if escolha == '4':
        posicao = int(input("Digite o índice que deseja saber: "))
        if 0 <= posicao < len(listaA):
            elemento = listaA[posicao]
            print(f"O elemento na posição {posicao} é {listaA[posicao]}")
        else:
            print("O índice digitado não existe na lista A")
        continue

    if escolha == '5':
        for elemento_A in listaA:
            try:
                if int(elemento_A) % 2 == 0:
                    listaB.append(elemento_A)
            except ValueError:
                pass
        print(listaB)
        continue

    if escolha == '6':
        for elemento in listaA:
            if len(elemento) == 2:
                listaC.append(elemento)
        print(listaC)
        continue

    if escolha == '7':
        print("Lista A:")
        for ind, elemento in enumerate(listaA):
            print(f"{ind} - {elemento}")

        print("Lista B:")
        for ind, elemento in enumerate(listaB):
            print(f"{ind} - {elemento}")

        print("Lista C:")
        for ind, elemento in enumerate(listaC):
            print(f"{ind} - {elemento}")
        
        continue
    if escolha == '8':
        break
