""" Exercício 3 """

# Faça um algoritmo que leia um texto e diga quantas 
# palavras existem neste texto.


txt = input("Digite um texto: ")

txt_separado = txt.split()
palavras = 0

for i in txt_separado:
    palavras += 1
    
print(f"Existem {palavras} nesse texto!")
