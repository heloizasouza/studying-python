# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:53:11 2024

@author: 00100712290

Seno, cosseno e tangente: leia um ângulo qualquer e mostre na tela o valor do 
seno, cosseno e tangente desse ângulo.
"""

# versão 1 - importa todo o módulo/pacote math

import math

an = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(an))
print('O ângulo {} têm o seno {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O ângulo {} têm o coseno {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O ângulo {} têm a tangente {:.2f}'.format(an, tan))


print('='*24)


# versão 2 - importa apenas os comandos interessados do módulo/pacote math

from math import radians, sin, cos, tan

an = float(input('Digite o ângulo: '))
sen = sin(radians(an))
print('O ângulo {} têm o seno {:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O ângulo {} têm o coseno {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ângulo {} têm a tangente {:.2f}'.format(an, tan))
