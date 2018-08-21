# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Digite a distância da viagem em Km: '))
if km <= 200:
    print('O valor da passagem é de R${:.2f}'.format(km * 0.5))
else:
    print('O valor da passagem é de R${:.2f}'.format(km * 0.45))
