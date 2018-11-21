# Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida, aplique 10% de desconto
# e imprima na tela tanto o valor total e também o valor com o desconto aplicado.

price = float(input("Digite o valor total da compra: R$"))

discount = price * 0.90

print("Valor total R$%.2f, valor com 10%% de desconto aplicado R$%.2f" % (price, discount))
