""" Exercício 3 """

# Ler dois valores numéricos e escrever a soma destes.
def soma_dois_numeros(a, b):
    soma = a + b
    return soma
n1 = int( input("Primeiro número: ") )
n2 = int( input("Segundo número: ") )
print("Soma=", soma_dois_numeros(n1, n2))
