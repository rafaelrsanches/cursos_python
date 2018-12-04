# Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido
# para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja
# que seja impresso:

start = int(input("Digite o primeiro número do intervalo: "))
end = int(input("Digite o último número do intervalo: "))

if start < end:
    for i in range(start, end):
        print(i)
else:
    print("O primeiro número precisa ser menor que o último número!")
