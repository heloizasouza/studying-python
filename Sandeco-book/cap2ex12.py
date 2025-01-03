'''
Calculadora Simples com Loop
É um programa que funciona como uma calculadora simples, ele solicita a quantidade de operações e 
permite ao usuário escolher entre adição, subtração, multiplicação e divisão. Em seguida solicita
dois números e exibe o resultado da operação escolhida.
'''

loop = int(input("Digite quantas vezes quer repetir o loop: "))

for i in range(loop):
    print(f'Loop, {i+1}')

    # input
    operacao = input("Digite a operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # output
    if operacao == "+":
        print(f'É uma soma e o resultado é: {num1 + num2}')
    elif operacao == "-":
        print(f'É uma diferença e o resultado é {num1 - num2}')
    elif operacao == "*":
        print(f'É uma multiplicação e o resultado é {num1 * num2}')
    else:
        print(f'É uma divisão e o resultado é {num1 / num2}')

