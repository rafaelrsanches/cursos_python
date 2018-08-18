# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

city = str(input('Digite o nome de uma cidade: ')).strip() # Lê o nome da cidade e retira os espaços excedentes
analysis = city.split() # Separa as palavras
print('SANTO' in analysis[0].upper()) # Põe as letras em maiúsculo e verifica se a primeira palavra é 'SANTO'
