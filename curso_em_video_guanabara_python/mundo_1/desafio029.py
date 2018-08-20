# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Digite a velocidade do carro em Km/h: ')) # Lê a velocidade do carro
if speed > 80: # Verifica se foi acima de 80Km/h
    ticket = (speed - 80) * 7 # Calcula o valor da multa
    print('Você ultrapassou o limite de velocidade de 80Km/h')
    print('Foi multado no valor de R${:.2f}, respeite as leis da próxima vez!'.format(ticket))
else:
    print('Tenha um bom dia! Dirija com segurança!')
