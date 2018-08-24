# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Analisando a existência de um triângulo.')
l1 = float(input('Digite a medida da primeira reta: '))
l2 = float(input('Digite a medida da segunda reta: '))
l3 = float(input('Digite a medida da terceira reta: '))

if (abs(l2 - l3) < l1 < l2 + l3) or (abs(l1 - l3) < l2 < l1 + l3) or (abs(l1 - l2) < l3 < l1 + l2):
    print('Triângulo válido!')
else:
    print('Não foi possível formar um triângulo com essas medidas =(')
