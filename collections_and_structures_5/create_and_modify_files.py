# COMO CRIAR E MODIFICAR ARQUIVOS:
# 'w' -> Usado somente para escever algo
# 'a' -> Usado para acrescentar algo 5
# 'r' -> Usado somente para ler algo
# 'r+' -> Usado para ler e escrever algo

import os

# EXAMPLE 1
with open('celulares.txt', 'w') as arquivo:
    arquivo.write('celular  2')

# EXAMPLE 2
nomes = ['lucas', 'carol', 'jeff', 'douglas']
numeros = [1, 2, 3, 4, 5, 6]


with open('nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)


with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)

# EXAMPLE 3
# to read what is inside the files
with open('nomes.txt', 'r', newline='') as arquivo:
    for linha in arquivo:
        print(linha)

# EXAMPLE 4
with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
        arquivo.write('9000')
