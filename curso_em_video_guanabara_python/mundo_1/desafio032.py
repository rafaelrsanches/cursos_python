# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date # Importa método para pegar a data atual do sistema

year = int(input('Qual ano deseja analisar? Digite 0 para analisar o ano atual: '))
if year == 0:
    year = date.today().year # Atribui o ano atual do sistema
if year % 4 == 0 and  year % 100 != 0 or year % 400 == 0: # Condições de um ano Bissexto
    print('{} é um ano Bissexto.'.format(year))
else:
    print('{} NÃO é um ano Bissexto.'.format(year))
