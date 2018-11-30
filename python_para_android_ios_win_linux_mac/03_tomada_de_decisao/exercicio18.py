# Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano. Por exemplo,
# se o usuário digitar a data 10/8 a mesma será inválida. Porém, caso a data seja 01/10/2018, a mesma
# deve ser considerada válida.

date = input("Digite a data no formato dd/mm/aaaa: ").strip()

if len(date) == 10:
    date = date.split("/")
    if (date[0] and date[1] and date[2]).isnumeric():
        print("Data válida!")
else:
    print("Data inválida!")
