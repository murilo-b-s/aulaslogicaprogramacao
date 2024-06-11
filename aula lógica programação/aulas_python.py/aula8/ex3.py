""" Desafio 3 """

# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.


         #
        ###
       #####
      #######
     #########
    ###########
   #############
  ###############
 #################
###################


qt_linha = int(input("Quantas linhas o triângulo deve ter? "))

for i in range(qt_linha + 1):
    print(" "*(qt_linha - i) + "#"*(i + (i-1)))