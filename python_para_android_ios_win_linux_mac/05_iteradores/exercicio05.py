# Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:

total = 0

for i in range(101):
    if i % 2 == 0:
        total += i

print("A soma dos números pares entre 0 e 100 é: {}".format(total))
