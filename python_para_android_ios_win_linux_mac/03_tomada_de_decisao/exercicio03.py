# Faça um algoritmo que leia dois números e imprima o maior.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O número %i é maior que %i!" % (num1, num2))
elif num2 > num1:
    print("O número %i é maior que %i!" % (num2, num1))
else:
    print("Os números são iguais!")
