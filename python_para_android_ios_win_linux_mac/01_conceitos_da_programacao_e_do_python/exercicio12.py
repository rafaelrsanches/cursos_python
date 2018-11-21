# Faça um algoritmo que solicite a largura e a altura de um retângulo. Em seguida, imprima para o usuário
# quantos metros quadrados possui a área total.

width = float(input("Digite a largura do retângulo: "))
height = float(input("Digite a altura do retângulo: "))

area = height * width

print("A área total é de %.2fm²" % area)
