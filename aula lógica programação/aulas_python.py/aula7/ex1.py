""" Exercício 1 """
# Faça um algoritmo que leia uma frase e diga quantas 
# vogais existem na frase digitada.(considerar apenas AaEeIiOoUu)


"""frase = input("Digite uma frase: ")
frase = frase.lower()"""

# tam = len(frase)
"""qt_vogais = 0"""

# for i in range(tam):
#     if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
#         vogais += 1
        
"""for caracter in frase:
    if caracter in ['a', 'e', 'i', 'o', 'u']:
        qt_vogais += 1
        
print(f"A quantidade de vogais é {qt_vogais}")"""



# MESMO CÓDIGO USANDO FUNÇÃO!!!!!!!!!!

def contar_vogais(frase):
    qt = 0
    vogais = "aeiou"
    for caracter in frase:
        if caracter in vogais:
            qt += 1 
    return qt

def ler_frase():
    return input("Digite uma frase: ")

frase_digitada = ler_frase()
qt_vogais = contar_vogais(frase_digitada)
print(f"A quantidade de vogais é {qt_vogais}")