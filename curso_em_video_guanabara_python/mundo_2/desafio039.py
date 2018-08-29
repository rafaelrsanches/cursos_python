# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai ser alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ywasborn = int(input('Digite o seu ano de nascimento: '))
years = int(date.today().year) - ywasborn

if years < 18:
    print('Faltam {} ano(s) para o alistamento militar.'.format(18 - years))
elif years == 18:
    print('Já está na hora de se alistar no serviço militar!')
else:
    print('Você já passou {} ano(s) do tempo de se alistar, vá regularizar sua situação!'.format(years - 18))
