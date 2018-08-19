# Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

name = str(input('Digite o nome completo: ')).strip().split() # Lê o nome, tira os espaços excedentes e separa as palavras
print('Primeiro = {}'.format(name[0])) # Mostra o primeiro nome
print('Último = {}'.format(name[len(name) - 1])) # Mostra o último nome
