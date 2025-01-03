# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:22:24 2024

@author: 00100712290

Sorteando um item da lista: Um professor quer sortear um dos seus quatro alunos
 para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos 
 e escrevendo na tela o nome do escolhido.
"""


from random import choice

a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
