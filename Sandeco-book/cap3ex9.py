'''
Este programa implementa um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100,
e o usuário tenta adivinhar o número. O programa fornece dicas como 'Maior' ou 'Menor' após cada tentativa, 
e limita o número de tentativas a 7, ao final do jogo exibe uma mensagem de sucesso ou falha.
'''

import random
print('Bem vindo, vamos jogar um jogo de adivinhação!')
print('Seu objetivo é acertar o número gerado pelo programa que está entre 1 e 100.')
print("Você tem 7 tentativas para acertar o número, e te ajudarei com dicas. Vamos lá?")
print('\n')

# gera um valor aleatorio entre 1 e 100
valor = random.randint(1, 100)

print('Valor gerado, qual seu primeiro chute?')
tentativas = 0
while tentativas < 7:
    chute = int(input('Digite seu chute:'))
    tentativas += 1

    if chute == valor:
        print(f'Parabéns você acertou o número {valor} em {tentativas} tentativas!')
        break
    elif chute < valor:
        print('Tente um valor maior!')
    else:
        print('Tente um valor menor!')

if chute != valor:
    print(f'Você falhou! O número correto era: {valor}')

print('Fim do jogo!')
