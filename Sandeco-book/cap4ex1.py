'''
Função chamada quadrado() que recebe um número como parâmetro e retorna o quadrado desse número.
'''

def quadrado(numero):
    return numero ** 2

valor = int(input("Digite o valor para ser elevado ao quadrado: "))
print(f'O quadrado de {valor} é {quadrado(valor)}')

