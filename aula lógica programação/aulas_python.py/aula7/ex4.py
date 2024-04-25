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

# if mes == 1:
#     print(f"{data[0]} de {meses[mes]} de {data[2]}")
    
# if mes == 2:
#     print(f"{data[0]} de Fevereiro de {data[2]}")

# if mes == 3:
#     print(f"{data[0]} de Março de {data[2]}")

# if mes == 4:
#     print(f"{data[0]} de Abril de {data[2]}")

# if mes == 5:
#     print(f"{data[0]} de Maio de {data[2]}")

# if mes == 6:
#     print(f"{data[0]} de Junho de {data[2]}")

# if mes == 7:
#     print(f"{data[0]} de Julho de {data[2]}")

# if mes == 8:
#     print(f"{data[0]} de Agosto de {data[2]}")

# if mes == 9:
#     print(f"{data[0]} de Setembro de {data[2]}")

# if mes == 10:
#     print(f"{data[0]} de Outubro de {data[2]}")

# if mes == 11:
#     print(f"{data[0]} de Novembro de {data[2]}")

# if mes == 12:
#     print(f"{data[0]} de Dezembro de {data[2]}")

