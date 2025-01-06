'''
Este programa recebe um texto e conta a frequência de cada palavra, ignorando maiúsculas e minúsculas.
O programa exibe uma lista de palavras únicas e o número de vezes que cada uma aparece no texto. 
Utilizando estruturas de dicionário e loops para realizar o processamento.
'''

# módulo com função que contém todos os caracteres de pontuação
import string

# Recebe o texto do usuário
texto = input('Digite um texto: ')

# Converte o texto para minúsculas
texto = texto.lower()
#  O método translate remove as pontuações que são identificadas pelo método string.punctuation 
texto = texto.translate(str.maketrans('', '', string.punctuation))

# Divide o texto em palavras
palavras = texto.split()

# Cria um dicionário para contar a frequência das palavras
frequencias = {}

# Contagem das palavras
for palavra in palavras:
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1

# Exibe as palavras e suas frequências
print("\nFrequência das palavras:")
for palavra, contagem in frequencias.items():
    print(f'{palavra}: {contagem}')
