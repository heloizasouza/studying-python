'''
Conversão de Temperatura
Crie um programa que solicite ao usuário uma temperatura em graus Celsius e a converta para Fahrenheit e Kelvin. 
Exiba os resultados para o usuário.
'''

celsius = float(input('Digite a temperatura em graus Celsius: '))
fahren = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f'{celsius}°C equivalem a {fahren}°F e a {kelvin} K')

