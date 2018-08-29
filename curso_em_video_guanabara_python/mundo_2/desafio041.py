# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

ywasborn = int(input('Digite a ano de nascimento do atleta: '))
age = (date.today().year) - ywasborn

print('O atleta tem {} anos.'.format(age))

if age <= 9:
    print('Categoria: MIRIM.')
elif age <= 14:
    print('Categoria: INFANTIL.')
elif age <= 19:
    print('Categoria: JUNIOR.')
elif age <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')
