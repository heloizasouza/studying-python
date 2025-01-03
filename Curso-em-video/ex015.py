# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:53:20 2024

@author: 00100712290

Aluguel de carros: pergunte a quantidade de Km percorridos por um carro alugado e 
a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar pelo aluguel é de R${}.'.format(dias*60+km*0.15))