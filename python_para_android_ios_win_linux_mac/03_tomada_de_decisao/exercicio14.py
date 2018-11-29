# Faça um algoritmo que leia três números e imprima-os em ordem crescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

b = [num1, num2, num3]
b.sort()

print(b)
