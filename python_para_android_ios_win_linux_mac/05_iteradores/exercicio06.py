# Faça um algoritmo que imprima os números primos entre 0 e 100:

for i in range(101):
    if (i == 2) or (i == 3) or (i == 5):
        print(i)
    elif (i == 1) or (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
        continue
    else:
        print(i)
