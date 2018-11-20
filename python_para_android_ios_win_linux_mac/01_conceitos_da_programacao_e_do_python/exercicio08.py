# Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie para a
# saída padrão a média:

num1 = float(input("Digite sua primeira nota: "))
num2 = float(input("Digite sua segunda nota: "))
num3 = float(input("Digite sua terceira nota: "))
num4 = float(input("Digite sua quarta nota: "))

average = (num1 + num2 + num3 + num4) / 4

print("Sua média é: %.2f" %average)
