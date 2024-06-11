
def exercicio1():
    print("Você escolheu a opção 1")
    print("Qual o seu nome?")
    nome = input()
    print(f"E aí, {nome}")
    idade = int(input("Qual tua idade?"))

    if idade > 0 and idade <= 14:
        print(f"{nome} Tu és uma criança ainda. Vai dormir!")
    elif idade > 14 and idade < 60:
        print("Fala Magrão. O que manda...")
    elif idade >= 60:
        print(f"{nome}, tu estas na 3a idade")
    else:
        print("Idade  inválida!")

def exercicio2():
    print("Você escolheu a opção 2.")
    frase = input("Digite uma frase: ")
    print(f"Esta frase possui {len(frase)} caracteres.")
    print("São eles: ")
    for caracter in frase:
        print(f">>> {caracter}")



while True:
    print("Menu de opções:")
    print("======================")
    print("0- Parar o programa")
    print("1- Exercício 1")
    print("2- Exercício 2")
    print("3- Exercício 3")
    print("4- Exercício 4")

    escolha = int(input())

    if escolha == 0:
        break

    if escolha == 1:
        exercicio1()

    if escolha == 2:
        exercicio2()

    if escolha == 3:
        pass

    if escolha == 4:
        pass




