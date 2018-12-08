# Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e
# permita que o mesmo possa definir 3 números que deverão ser ignorados, ou seja,
# que não serão impressos na tela:

num1 = int(input("Digite o número inicial: "))
num2 = int(input("Digite o número final: "))
print("-" * 25)
ignore_num1 = int(input("Digite o primeiro número a ser ignorado: "))
ignore_num2 = int(input("Digite o segundo número a ser ignorado: "))
ignore_num3 = int(input("Digite o terceiro número a ser ignorado: "))

for i in range(num1, (num2 + 1)):
    if i not in(ignore_num1, ignore_num2, ignore_num3):
        print(i)
