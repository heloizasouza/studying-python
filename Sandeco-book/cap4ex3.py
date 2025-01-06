'''
Programa da função contar_vogais() que recebe uma string como parâmetro e retorna o número de vogais presentes nessa string.
'''

def contar_vogais(texto):
    vogais = 'aeiou'
    texto = texto.lower()
    return sum([1 for letra in texto if letra in vogais])


def conta_consoantes(texto):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    texto = texto.lower()
    return sum([1 for letra in texto if letra in consoantes])


texto = input('Digite um texto: ')
print(f'Número de vogais no texto: {contar_vogais(texto)}')
print(f'Número de consoantes no texto: {conta_consoantes(texto)}')

