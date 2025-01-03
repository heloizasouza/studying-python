'''
O programa lê uma lista de nomes separados por vírgula e exibe cada nome em uma nova linha em ordem alfabética.
'''

nomes = input("Digite os nomes separados por vírgula: ")
nomeSplit = nomes.split(",")
nomeSplit.sort()
for nome in nomeSplit:
    print(nome)


