""" Exercício 2 """
# Faça um algoritmo que leia um texto com até 20 caracteres, 
# e imprima esse texto de traz para frente.

while True:
    txt = input("Digire um texto de até 20 caracteres: ")
    tam = len(txt)
    if tam > 20:
        print("Por favor, digite um texto de no máximo 20 caracteres!")
        continue
    else:
        break
for i in range(tam-1, -1, -1):
    print(txt[i], end = "")

print(txt[::-1])