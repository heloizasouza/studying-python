# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:57:02 2024

@author: 00100712290

Exiba o dobro, triplo e a raiz quadrada do valor de input
"""

valor = int(input('Digite um valor: '))
print('O dobro desse valor é: {} \nO triplo desse valor é: {} \nA raiz quadrada desse valor é: {:.2f}'.format(valor*2, valor*3, valor**(1/2)))

# :.2f significa --> depois do ponto flutuante use 2 casas após o decimal