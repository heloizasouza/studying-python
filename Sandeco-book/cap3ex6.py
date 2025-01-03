'''
Programa que calcula o fatorial de um inteiro positivo usanso o loop while.
'''

n = int(input("Digite um número inteiro positivo: "))

fatorial = 1
i = 1

if n == 0 or n == 1:
    print(f"O fatorial de {n} é {fatorial}")
else:
    while i <= n:
        fatorial *= i
        i += 1
    print(f"O fatorial de {n} é {fatorial}")

