''' Exercício 5 '''


def soma_cinco(a, b, c, d, e):
    soma = a + b + c + d + e
    return soma

num1 = int( input('Digite o primeiro número: '))
num2 = int( input('Digite o segundo número: '))
num3 = int( input('Digite o terceiro número: '))
num4 = int( input('Digite o quarto número: '))
num5 = int( input('Digite o cinco número: '))

soma = num1 + num2 + num3 + num4 + num5

print('A soma dos valores é: ', soma_cinco(num1, num2, num3, num4, num5))
print('A média dos valores é: ', (soma / 5))

