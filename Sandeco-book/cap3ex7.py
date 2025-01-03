'''
O programa lê as notas de uma turma de 5 alunos, armazena essas notas em uma lista, calcula a média da turma e a quantidade de alunos acima da média.
'''

notas = []
soma = 0
media = 0
acimaMedia = 0

for i in range(5):
    notas.append(float(input(f"Digite a nota do aluno {i + 1}: ")))
    soma += notas[i]

media = soma / 5

for nota in notas:
    if nota >= media:
        acimaMedia += 1

print(f"A média das notas da turma é {media}")
print(f"A quantidade de alunos acima da média da turma é {acimaMedia}")
print(f"A quantidade de alunos abaixo da média da turma é {5 - acimaMedia}")

