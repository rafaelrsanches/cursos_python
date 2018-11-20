# Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida, converta essa medida para centímetros
# e envie para a saída padrão:

m = float(input("Digite a medida em metros: "))

cm = m * 100

print("A medida %.2fm convertido em centímetros é %.2fcm" % (m, cm))
