# Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Qual é o salário do funcionário? R$'))
if salary > 1250.00:
    print('Com o aumento de 10% o salário passará a ser R${:.2f}'.format(salary * 1.10))
else:
    print('Com o aumento de 15% o salário passará a ser R${:.2f}'.format(salary * 1.15))
