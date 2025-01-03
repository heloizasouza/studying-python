# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:10:44 2024

@author: 00100712290

Calculando descontos: leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

valor = float(input('Qual é o preço do produto? R$'))
print('O produto custava R${}, com 5% de desconto ele custa R${:.2f}.'.format(valor, valor - (valor*0.05)))