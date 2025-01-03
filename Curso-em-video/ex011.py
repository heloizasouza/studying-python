# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:58:56 2024

@author: 00100712290

Pintando parede: leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
print('Sua parede tem a dimensão {}x{} e sua área é de {:.2f} metros quadrados.'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(area/2))