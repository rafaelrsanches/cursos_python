# Faça um algoritmo que peça um valor numérico. Em seguida, verifique se o número é inteiro ou decimal.

num = float(input("Digite um valor numérico: "))

if num % 1 == 0:
    print("O valor é um número inteiro!")
else:
    print("O valor é um número decimal!")
