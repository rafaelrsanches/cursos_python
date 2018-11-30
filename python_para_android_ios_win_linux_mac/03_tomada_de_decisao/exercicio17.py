# Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome
# do mês correspondente. Por exemplo, se for informado o número 2, o algoritmo deverá exibir: fevereiro.
# O algoritmo também deve validar se a entrada está correta.

month = float(input("Digite o número do mês: "))

if (month % 1 == 0) and (month >= 1) and (month <= 12):
    if month == 1:
        print("Janeiro")
    elif month == 2:
        print("Fevereiro")
    elif month == 3:
        print("Março")
    elif month == 4:
        print("Abril")
    elif month == 5:
        print("Maio")
    elif month == 6:
        print("Junho")
    elif month == 7:
        print("Julho")
    elif month == 8:
        print("Agosto")
    elif month == 9:
        print("Setembro")
    elif month == 10:
        print("Outubro")
    elif month == 11:
        print("Novembro")
    elif month == 12:
        print("Dezembro")
else:
    print("O número não corresponde a um mês do ano.")
