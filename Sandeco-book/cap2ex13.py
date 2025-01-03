

real = float(input('Digite a quantia em reais (BRL): '))
cotacao = float(input('Digite a cotação do dólar (USD): '))

dolar = real / cotacao

print(f'R${real} equivalem a US${dolar:.2f}')


