# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:45:11 2024

@author: 00100712290

Catetos e hipotenusa:  leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

# versão 1 - calculando manualmente

from math import sqrt

cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(sqrt(pow(cato, 2)+pow(cata, 2))))


# versão 2 - usando comando 

from math import hypot

cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(cato, cata)))
