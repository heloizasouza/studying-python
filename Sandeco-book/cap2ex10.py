''' *Contagem de Caracteres* 
Escreva um programa que peça ao usuário para digitar uma frase e conte quantos caracteres, palavras, letras maiúsculas e caracteres especiais há na frase.
'''

#  input
frase = input("Digite uma frase: ")

# contagem de caracteres
qtd_chr = len(frase)

# contagem de palavras
qtd_words = len(frase.split())

# contagem de letras maiúsculas
qtd_upper = sum(1 for char in frase if char.isupper())

# contagem de caracteres especiais
special_characters = "!@#$%^&*()-+?_=,<>/"
qtd_special = sum(1 for char in frase if char in special_characters)

# output
print("Nessa frase temos:\n", qtd_chr, "caracteres,\n", qtd_upper, "letras maiúsculas,\n", qtd_words, "palavras e\n", qtd_special, "caracteres especiais.")
