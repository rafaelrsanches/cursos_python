# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

name = str(input('Digite o nome: ')).strip() # Lê o nome e retira os espaços excedentes
print('SILVA' in name.upper()) # Verifica se tem 'SILVA' na string upper (em letras maiúsculas)
