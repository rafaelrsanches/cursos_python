# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

name = str(input('Digite o nome: ')).strip() # Lê o nome e retira os espaços excedentes
name_analysis = name.upper().split() # Pôe tudo em maiúsculo e separa as palavras
print('SILVA' in name_analysis)
