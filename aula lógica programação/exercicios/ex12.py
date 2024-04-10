""" Exercício 12 """

# Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã.
# Dados extras:
# - Distância da casa de Maria até sua irmã : 520 km
# - Seu carro consome 12 Km/litro de combustível.
# - Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.
# Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para aviagem e o custo da viagem.

def valorViagem(dist, cons, preco):
    calculo = (dist / cons) * preco
    return calculo

def litros(dist, cons):
    calculo = (dist / cons)
    return calculo

dist = int(input("Digite a distância da viagem: "))
cons =  int(input("Digite a média de consumo do carro em km/l: "))
preco = int(input("Digite o preço do combustível: "))

# print("Para essa viagem será necessário", litros(dist, cons), "litros de combustível")

print(f"Para essa viagem será necessário {litros(dist, cons)} litros de combustível")

# print("Custo total da viagem: R$", valorViagem(dist, cons, preco))

print(f"Custo total da viagem: R$ {valorViagem(dist, cons, preco)}")