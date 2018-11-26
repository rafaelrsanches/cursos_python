# Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.

num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo!")
elif num < 0:
    print("O número é negativo!")
elif num == 0:
    print("O número é zero!")
