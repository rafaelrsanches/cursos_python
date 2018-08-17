# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras no total(sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome completo: ')).strip() #Leitura do nome
print('Analisando seu nome...')
first_name = name.split()
print('Seu nome em maiúsculas é {}'.format(name.upper())) #Mostra o nome em letras maiúsculas
print('Seu nome em minúsculas é {}'.format(name.lower())) #Mostra o nome em letras minúsculas
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' '))) #Mostra o número de letras
print('Seu primeiro nome é {} e tem {} letras'.format(first_name[0], len(first_name[0]))) #Mostra o número de letras do primeiro nome
