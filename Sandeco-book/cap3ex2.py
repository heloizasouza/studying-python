'''
Este é um programa que solicita uma palavra e conta quantas letras 'a' ou 'A' estão presentes nela.
'''

word = input('Digite uma palavra: ')
count = 0

for letter in word:
    if letter == 'a' or letter == 'A':
        count += 1

print(f'A palavra possui {count} letras "a" ou "A".')