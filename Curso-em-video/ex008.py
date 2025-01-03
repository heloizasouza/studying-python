# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:06:56 2024

@author: 00100712290

Construa um conversor de medidas
"""

valor = int(input('Digite uma distância em metros: '))
print('Tem-se {} km \nTem-se {} hm \nTem-se {} dam'.format(valor/1000, valor/100, valor/10))
print('Tem-se {} dm \nTem-se {} cm \nTem-se {} mm'.format(valor*10, valor*100, valor*1000))