"""
Para o exercício considere as seguintes listas: 
listaA, listaB, listaC
Você tem um código funcional mas parcial que mostra
um menu com várias opções. 
Você deverá finalizar o código implementando 
as opções que faltam.
"""


def transforma_numeros(elemento):
    try:
        int(elemento)
        return True
    except ValueError:
        return False

menu = """
    ========================================
    1- Adicionar um elemento na listaA
    2- Retirar um elemento na listaA
    3- Digite um número e mostre sua posição 
        na listaA
    4- Digite uma posição e diga qual o número 
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
lista_numeros = []

listaA = ['6', '4', '5', '89','amoeba', '4']
while True:
    print(menu)
    escolha = input("Escolha: ")
    if escolha == '1':
        elemento = input("Digite o que deseja adicionar à lista A: ")
        if elemento.isdigit():
            listaA.append(int(elemento))
        else:
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
        elemento = input("Digite o número: ")
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
            print(elemento)
        else:
            print("O índice digitado não existe na lista A")
        continue

    if escolha == '5':
        for i in listaA:
            if i == int:
                if i%2 == 0:
                    listaB.append(i)
        print(listaB)
        pass
    if escolha == '6':
        # seu código aqui
        pass
    if escolha == '7':
        # seu código aqui
        pass
    if escolha == '8':
        # seu código aqui
        pass


while True:
    escolha = input("Escolha: ")
    if escolha == '5':
        # seu código aqui
        tem_par = False

        for elemento_A in listaA:
            try:
                if int(elemento_A) % 2 == 0:  # significa que o número é par
                    listaB.append(elemento_A)
                    tem_par = True
            except ValueError:
                pass
        if tem_par == True:
            print(listaB)
        else:
            print("Não há elementos pares na listaA.")

