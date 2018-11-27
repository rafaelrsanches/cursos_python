# Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos
# anos sua mãe o teve.

your_age = int(input("Digite a sua idade: "))
mother_age = int(input("Digite a idade da sua mãe: "))

print("Sua mãe o teve com %i anos." % (mother_age - your_age))
