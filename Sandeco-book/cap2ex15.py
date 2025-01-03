'''
Calculadora de Média Ponderada 
É um programa que calcula a média ponderada de três notas, onde o usuário informa as notas e seus respectivos pesos.
'''

# Solicita as notas e os pesos
notas = [float(input(f'Digite a {i+1}º nota: ')) for i in range(3)]
pesos = [float(input(f'Digite o peso da {i+1}º nota: ')) for i in range(3)]

# Calcula a média ponderada
media = sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)

# Exibe o resultado
print(f'A média ponderada é {media:.2f}')


'''
**Descrição do Código**
O comando **[float(input(f'Digite a {i+1}ª nota: ')) for i in range(3)]** é uma compreensão de lista em Python. 

Uma compreensão de lista é uma forma concisa de criar listas em Python. 
Ela permite gerar listas de maneira mais compacta e legível, geralmente em uma única linha de código.

A sintaxe básica de uma compreensão de lista é:

[expressão for item in iterável]

No caso do comando **, ele está criando uma lista com os valores que são obtidos do usuário, convertendo esses valores para float.
'''
