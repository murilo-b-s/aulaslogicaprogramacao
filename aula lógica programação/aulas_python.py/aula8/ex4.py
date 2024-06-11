""" Desafio 4 """

# Crie um código que imprima o retângulo abaixo.
# lendo a quantidade de linhas e colunas.
# Utilize o comando for

##########
#        #
# ###### #
# #    # #
# #    # #
# #    # #
# #    # #
# #    # #
# ###### #
#        #
##########

linha = int(input("Digite a quantidade de linhas do quadrado: "))
coluna = int(input("Digite a quantidade de colunas do quadrado: "))

linha_pequeno = linha - 4
coluna_pequeno = coluna - 6

def quadrado_grande(valor):
    for i in range(coluna):
        if i == 0 or i == linha -1:
            print("#"*coluna)
        elif i == 2 or i == linha -2:
            print("#", "", "#"* (coluna_pequeno), " ", "#")
        else:
            print("#", " ", "#", " "*(coluna -2), "#", " ", "#")

def quadrado_pequeno(valor2):
    for i in range(coluna):
        if i == 3 or i == -3:
            print(" "* 2, "#"* coluna)
        else: print(" "* 2, "#", " "*(coluna_pequeno - 2), "#")

quadrado_grande(coluna)

