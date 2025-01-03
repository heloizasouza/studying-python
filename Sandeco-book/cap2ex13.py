'''
Conversão de Moeda
Crie um programa que pergunte ao usuário a quantia em reais (BRL) e a taxa de câmbio atual para dólares (USD).
Calcule e exiba o valor convertido em dólares.
'''

real = float(input('Digite a quantia em reais (BRL): '))
cotacao = float(input('Digite a cotação do dólar (USD): '))

dolar = real / cotacao

print(f'R${real} equivalem a US${dolar:.2f}')


