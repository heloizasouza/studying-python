'''
Este programa simula um caixa eletrônico. Ele permite que o usuário insira o valor de saque desejado (em múltiplos de 10) e exibe quantas cédulas
de cada denominação (R$100, R$50, R$20, R$10) serão necessárias para totalizar o valor do saque, utilizando o menor número possível de cédulas.
'''

saque = int(input('Digite o valor desejado de saque (múltiplos de 10): '))

# Verifica se o valor do saque é múltiplo de 10
if saque % 10 != 0:
    print('Valor de saque inválido! Por favor, insira um valor múltiplo de 10.')
else:
    # Inicializando as variáveis para as quantidades de cédulas
    cedulas_100 = cedulas_50 = cedulas_20 = cedulas_10 = 0

    # Determina a quantidade de cédulas de R$100
    cedulas_100 = saque // 100
    saque %= 100  # Atualiza o valor do saque com o restante

    # Determina a quantidade de cédulas de R$50
    cedulas_50 = saque // 50
    saque %= 50  # Atualiza o valor do saque com o restante

    # Determina a quantidade de cédulas de R$20
    cedulas_20 = saque // 20
    saque %= 20  # Atualiza o valor do saque com o restante

    # Determina a quantidade de cédulas de R$10
    cedulas_10 = saque // 10
    saque %= 10  # Atualiza o valor do saque com o restante (deve ser 0 no final)

    # Exibe as quantidades de cédulas utilizadas
    if cedulas_100 > 0:
        print(f'São necessárias {cedulas_100} cédulas de R$100.')
    if cedulas_50 > 0:
        print(f'São necessárias {cedulas_50} cédulas de R$50.')
    if cedulas_20 > 0:
        print(f'São necessárias {cedulas_20} cédulas de R$20.')
    if cedulas_10 > 0:
        print(f'São necessárias {cedulas_10} cédulas de R$10.')

    # Caso o valor de saque tenha sido completamente dividido em cédulas
    if saque == 0:
        print('Saque realizado com sucesso!')
    else:
        print('Erro no saque!')  # Caso o valor não tenha sido completamente dividido
