'''
Comparação de Idades 
Escreva um programa que peça ao usuário para inserir duas idades e compare qual delas é maior, menor ou se são iguais, 
mostrando mensagens adequadas para cada situação
'''

# Solicita duas idades
idade1 = int(input('Digite a primeira idade: '))
idade2 = int(input('Digite a segunda idade: '))

# Compara as idades
if idade1 > idade2:
    print('A primeira idade é maior que a segunda')
elif idade1 == idade2:
    print('As idades são iguais')
else:
    print('A segunda idade é maior que a primeira')


