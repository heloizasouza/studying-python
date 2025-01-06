'''
Programa da função maior_numero() que recebe três números como parâmetros e retorna o maior deles.
'''

def maior_numero(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
      return num3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(f'O maior número é: {maior_numero(num1, num2, num3)}')

