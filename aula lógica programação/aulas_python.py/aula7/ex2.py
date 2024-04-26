""" Exercício 2 """
# Faça um algoritmo que leia um texto com até 20 caracteres, 
# e imprima esse texto de traz para frente.

# while True:
#     txt = input("Digire um texto de até 20 caracteres: ")
#     tam = len(txt)
#     if tam > 20:
#         print("Por favor, digite um texto de no máximo 20 caracteres!")
#         continue
#     else:
#         break
# for i in range(tam-1, -1, -1):
#     print(txt[i], end = "")

# print(txt[::-1])


# MESMO CÓDIGO USANDO FUNÇÃO!!!!!!!!!!


def ler_texto():
    while True:
        txt = input("Digire um texto de até 20 caracteres: ")
        if len(txt) >= 20:
            print(f"Máximo 20 caracteres!")
        else: return txt       

def imprimir(txt):
    print("Imprimindo de trás pra frente!")
    return print(txt_ok[::-1])

txt_ok = ler_texto()
imprimir(txt_ok)

