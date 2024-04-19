""" Exercício 1 """
# Faça um algoritmo que leia uma frase e diga quantas 
# vogais existem na frase digitada.(considerar apenas AaEeIiOoUu)


frase = input("Digite uma frase: ")
frase = frase.lower()

# tam = len(frase)
vogais = 0

# for i in range(tam):
#     if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
#         vogais += 1
        
for caracter in frase:
    if caracter in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
        
print(f"A quantidade de vogais é {vogais}")
