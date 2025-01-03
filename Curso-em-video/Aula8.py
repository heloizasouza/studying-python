# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:26:58 2024

@author: 00100712290

Aula 8 - utilizando módulos
"""
# assim importa toda a biblioteca
import math
# assim importa uma função da biblioteca
from math import sqrt


num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))


