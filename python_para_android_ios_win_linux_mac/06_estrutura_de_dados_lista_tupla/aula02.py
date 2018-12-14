# Exemplo Prático com Operador In

# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um número: "))
#
# if x in [a, b, c]:
#     print("Está contido!")
# else:
#     print("NÃO está contido!")

# ------------------------------------------------

cores = ["azul", "amarelo", "vermelho", "branco"]

while True:
    cor = input("Digite uma cor, ou '0' para sair do programa: ").lower().strip()

    if cor == "0":
        break
    elif cor in cores:
        print("Essa cor está contida!")
    else:
        print("Essa cor NÃO está contida!")

    print()
