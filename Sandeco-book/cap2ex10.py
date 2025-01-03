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


'''
**Detalhes do código:**
O comando **sum(1 for char in frase if char.isupper())** em Python é uma forma compacta de contar o número de letras maiúsculas em uma string (frase). 

Analisando o que está acontecendo em cada parte:
for char in frase: Este é um loop que percorre cada caractere da string 'frase'. A variável 'char' representa cada caractere individualmente.

if char.isupper(): Esse é um filtro condicional que verifica se o caractere 'char' é uma letra maiúscula. 
A função isupper() retorna True se o caractere for maiúsculo e False caso contrário.

1 for char in frase if char.isupper(): Quando o filtro if char.isupper() é True, a expressão 1 é executada. 
Ou seja, sempre que um caractere maiúsculo é encontrado, o valor 1 é gerado. Para cada letra maiúscula, um 1 é somado.

sum(...): A função sum() soma todos os valores gerados pela expressão dentro dos parênteses. 
Então, a cada vez que um caractere maiúsculo for encontrado, o valor 1 é somado ao total. 
No final, você obterá a contagem total de letras maiúsculas na string.
'''