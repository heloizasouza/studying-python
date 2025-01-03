# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:38:42 2024

@author: 00100712290

Quebrando um número: leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

from math import trunc

valor = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua proporção inteira é {}'.format(valor, trunc(valor)))