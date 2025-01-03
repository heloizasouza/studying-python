'''
Reverso de String
Escreva um programa que solicite ao usuário uma string e exiba o reverso dessa string.
'''

string = input('Digite uma string: ')
reverso = string[::-1]
print(reverso)


'''
**Detalhes do código:**
[::-1]:
O que está entre os colchetes ([]) é um fatiamento (ou "slicing") da string.
O fatiamento pode ser descrito como **string[inicio:fim:passo]**, onde:
inicio: índice onde a fatia começa.
fim: índice onde a fatia termina (não inclui o índice de término).
passo: a distância entre os índices consecutivos para cada item.

No caso específico de [::-1]:
O índice de início e o índice de fim não são especificados, o que significa que a fatia começa do começo da string e vai até o final.
O passo -1 é o que inverte a ordem dos caracteres. Em vez de percorrer a string da esquerda para a direita (passo positivo), 
o passo -1 faz com que a string seja percorrida da direita para a esquerda, resultando na string invertida.
'''