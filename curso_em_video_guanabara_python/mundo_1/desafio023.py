# Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

n = int(input('Digite um número: ')) #Leitura do número

print('Unidade: {}'.format((n // 1) % 10)) #Mostra o número de unidades
print('Dezena: {}'.format((n // 10) % 10)) #Mostra o número de dezenas
print('Centena: {}'.format((n // 100) % 10)) #Mostra o número de centenas
print('Milhar: {}'.format((n // 1000) % 10)) #Mostra o número de milhares
