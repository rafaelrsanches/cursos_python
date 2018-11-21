# Faça um algoritmo que solicite ao usuário digitar 2 números. Em seguida, imprima o total decimal da divisão
# e o total inteiro (sem casas decimais):

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

td = num1 / num2
ti = num1 // num2

print("Total decimal: %f" % td)
print("Total inteiro: %i" % ti)
