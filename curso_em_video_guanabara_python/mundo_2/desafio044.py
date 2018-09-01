# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

price = float(input('Qual o valor do produto? R$'))
payment = int(input('''[1] - Dinheiro
[2] - Cheque
[3] - Cartão de Crédito
Qual a forma de pagamento? '''))

if payment == 1 or payment == 2:
    print('O preço final do produto será de R${:.2f}, com 10% de desconto!'.format(price * 0.90))
else:
    parcela = int(input('Em quantas parcelas prefere pagar? '))

    if parcela == 1:
        print('O preço final do produto será de R${:.2f}, com 5% de desconto!'.format(price * 0.95))
    elif parcela == 2:
        print('O preço final do produto será de R${:.2f}'.format(price))
    else:
        print('O preço final do produto será de R${:.2f}'.format(price * 1.20))
