# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:36:22 2024

@author: 00100712290

Leia um input do usuário e informe todas as características desse input
"""


n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Nada foi digitado?', n.isspace())
print('É alfabético?', n.isalpha())
print('É numérico?', n.isnumeric())
print('É alfanumérico?', n.isalnum())
print('Está tudo em letras maiúsculas?', n.isupper())
print('Está tudo em letras minúsculas?', n.islower())
print('Está capitalizado?', n.istitle())