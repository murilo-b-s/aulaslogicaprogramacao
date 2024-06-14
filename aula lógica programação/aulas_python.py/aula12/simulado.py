"""
Competências a serem avaliadas:
- Conhecer os comandos da linguagem
- Saber utilizar os comandos corretamente
- Desenvolver uma solução viável para a atividade proposta
- Códigos iguais = D

Faça um algoritmo que leia o nome, a idade e o genero
de pelo menos 5 pessoas.
OBS: para o gênero aceitar a digitação apenas de F ou M.

Armazene esses dados nas listas: lst_nome, lst_idade e lst_genero.
Encerre a digitação quando for digitado a palavra 'fim' no nome da
pessoa.
Após imprima as seguintes informações:
-> Média de idades das pessoas
-> Nome da pessoa mais velha
-> Percentual de pessoas do gênero Feminino

"""


############## VALENDO NOTA ###################

lst_nome = []
lst_idade = []
lst_genero = []

contador = 0
while True:

    nome = input('Digite um nome ou "FIM" se quiser parar: ').capitalize()
    if nome == 'Fim':
        if contador >= 5:
            break
        else:
            print('Digite no mínimo 5 nomes.')
            continue
    else:
        lst_nome.append(nome)
        contador += 1
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            lst_idade.append(idade)
            break
        except ValueError:
            print("Digite apenas valores numéricos.")

    while True:
        genero = input('Digite o seu gênero no formato F/M: ').upper()
        if genero == 'F' or genero == 'M':
            lst_genero.append(genero)
            break
        else:
            print('Opção inválida. Digite no formato F/M.')
            continue

media_idade  = sum(lst_idade)/len(lst_idade)
print(f"A média de idade das pessoas é de {media_idade:.2f}")

mais_velho = max(lst_idade)


posicao = lst_idade.index(mais_velho)
print(f"{lst_nome[posicao]} é a pessoa mais velha.")


qtd_feminino = lst_genero.count('F')
porcentagem = qtd_feminino/len(lst_genero)*100
print(f"A porcentagem de gênero feminino é de {porcentagem:.2f}%")
