# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - Média abaixo de 5.0 = REPROVADO
# - Média entre 5.0 e 6.9 = RECUPERAÇÃO
# - Média 7.0 ou superior = APROVADO

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
average = (n1 + n2) / 2

if average < 5.0:
    print('Você está REPROVADO com a média {:.2f}'.format(average))
elif 5 <= average <= 6.9:
    print('Você está de RECUPERAÇÃO com a média {:.2f}'.format(average))
else:
    print('Você está APROVADO com a média {:.2f}'.format(average))
