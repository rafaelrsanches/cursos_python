# Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 < num2:
    print("O número %i é menor que %i!" % (num1, num2))
elif num2 < num1:
    print("O número %i é menor que %i!" % (num2, num1))
else:
    print("Os números são iguais!")
