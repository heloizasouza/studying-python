# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:22:00 2024

@author: 00100712290

Reajuste salarial: leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

sal = float(input('Qual o seu salário: R$'))
print('Seu novo salário, com aumento de 15%, é de R${:.2f}.'.format(sal*1.15))