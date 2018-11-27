# Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então,
# se a mesma é de menor.

age = int(input("Digite sua idade: "))

if age >= 18:
    print("Você já é maior de idade!")
elif (age >= 0) and (age < 18):
    print("Você é menor de idade!")
else:
    print("Idade inválida!")
