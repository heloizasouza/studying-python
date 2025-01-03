'''
É solicitado ao usuário um número inteiro e é verificado se ele é positivo, negativo ou nulo.
'''

num = int(input('Digite um número: '))

if num == 0:
    print('O número é nulo.')
elif num > 0:
    print('O número é positivo.')
else:
    print('O número é negativo.')