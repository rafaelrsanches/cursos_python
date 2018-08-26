# Escreva um programa para aprovar o empréstimo bancário para a compra de um imóvel. O programa vai perguntar o valor
# do imóvel, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

house = float(input('Digite o valor do imóvel: R$'))
salary = float(input('Digite o salário do comprador: R$'))
years = int(input('Em quantos anos o comprador deseja pagar? '))
colors = {'clear': '\033[m',
          'boldred': '\033[1;31m',
          'boldgreen': '\033[1;32m'}

monthly = house / (years * 12)
if monthly > (salary * 0.30):
    print('Empréstimo {}NEGADO{}!!!'.format(colors['boldred'], colors['clear']))
else:
    print('Empréstimo {}APROVADO{}!!!'.format(colors['boldgreen'], colors['clear']))
