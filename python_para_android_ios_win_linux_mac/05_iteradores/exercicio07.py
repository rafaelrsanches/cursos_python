# Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:

num1 = int(input("Digite o número inicial: "))
num2 = int(input("Digite o número final: "))

primos = [2, ]
primos_escolhidos = []

if num1 < 3:
    primos_escolhidos.append(2)

for primo in range(3, (num2 + 1)):
    considerado = True

    for numero in primos:
        if primo % numero == 0:
            considerado = False
            break

    if considerado:
        primos.append(primo)
        if primo >= num1:
            primos_escolhidos.append(primo)

print(primos_escolhidos)
