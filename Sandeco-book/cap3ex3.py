'''
Um programa que recebe a idade e determina se a pessoa é menor de idade, adulta ou idosa.
'''


idade = int(input("Informe sua idade: "))

if idade< 18:
    print("Você é menor de idade!")
elif idade >= 65:
    print("Voce é idoso!")
else:
    print("Você é adulto!")

