# Faça um algoritmo que verifica se um determinado valor é um número inteiro.

num = float(input("Digite um valor: "))

if num % 2 == 0 or num % 2 == 1:
    print("O valor é um número inteiro!")
else:
    print("O valor não é um número inteiro!")
