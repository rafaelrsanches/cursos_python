n = float(input('Quanto dinheiro você tem para as compras no exterior? R$'))

print('Com R${:.2f} você poderá comprar US${:.2f} ou €{:.2f}'.format(n, n/3.86, n/4.41))
