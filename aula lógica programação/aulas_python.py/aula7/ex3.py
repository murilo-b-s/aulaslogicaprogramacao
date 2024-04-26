""" Exercício 3 """

# Faça um algoritmo que leia um texto e diga quantas 
# palavras existem neste texto.


# txt = input("Digite um texto: ")

# txt_separado = txt.split()
# palavras = 0

# for i in txt_separado:
#     palavras += 1
    
# print(f"Existem {palavras} nesse texto!")



# MESMO CÓDIGO USANDO FUNÇÃO!!!!!!!!!!



def ler_texto():
    return input("Digite um texto: ")

def converter_em_lista(texto):
    return texto.split()

def contar_palavras(lista):
    return len(lista)

def imprimir_mensagem(qt_palavras):
    print(f"A quantidade de palavras é {qt_palavras}")
    
imprimir_mensagem(contar_palavras(converter_em_lista(ler_texto())))
