# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:29:44 2024

@author: 00100712290

Conversor de Temperaturas: converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

temp = float(input('Informe a temperatura em °C: '))
print('A temperatura de {}°C corresponde a {:.1f}°F!'.format(temp, (temp*9/5)+32))