# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:52:20 2024

@author: 00100712290

Conversor de real para dolar
"""

valor = float(input('Quantos reais você têm na carteira? R$'))
print('Se você têm {} reais então você pode comprar {:.2f} dólares.'.format(valor, valor/3.27))