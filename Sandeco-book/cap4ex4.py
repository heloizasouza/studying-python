'''
Programa da função calcular_potencia() que recebe dois parâmetros, base e expoente, e retorna o resultado da base elevada ao expoente.
'''

def calcular_potencia(base, expo):
    return base ** expo

# Testando a função
base = int(input('Digite a base da potência a ser calculada: '))
expo = int(input('Digite o expoente da potência a ser calculada: '))

print(f'{base} elevada a {expo} é igual a {calcular_potencia(base, expo)}')