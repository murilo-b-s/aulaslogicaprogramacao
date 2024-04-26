""" Exercício 4 """
# Faça um algoritmo que leia uma string no formato de data (dd/mm/aaaa)
# e escreva esta com o nome do mês por extenso.
# Exemplo: 
# entrada: 10/04/2024
# saida : 10 de abril de 2024.


while True:

    data_digitada = input("Digite uma a data desejada no formato dd/mm/aaaa: ")

    meses = [" ", "Janeiro", "Fevereiro", "Março","Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    data = data_digitada.split("/")
    mes = int(data[1])
    dia = int(data[0])



    if dia > 31 or dia < 1:
        print("Data inválida!")
        continue

    elif mes > 12 or mes < 1:
        print("Data inválida!")
        continue
    
    else:
        break

    
print(f"{data[0]} de {meses[mes]} de {data[2]}")

