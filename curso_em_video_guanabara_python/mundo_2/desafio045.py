# Crie um programa que faça o computador jogar JOKEMPÔ com você.

from time import sleep
from random import randint

print('-=' *10, ' JOKEMPÔ GAME', '=-' * 10)
play = int(input('''[1] - Pedra
[2] - Papel
[3] - Tesoura
Qual sua jogada? '''))

playmachine = randint(1, 3)

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ!!!')
sleep(1)

if play == 1:
    if playmachine == 1:
        print('EMPATOUUU!!! Também escolhi Pedra')
    elif playmachine == 2:
        print('GANHEIII DE VOCÊ!!! Escolhi Papel')
    else:
        print('DESSA VEZ EU PERDI!!! Escolhi Tesoura')
elif play == 2:
    if playmachine == 1:
        print('DESSA VEZ EU PERDI!!! Escolhi Pedra')
    elif playmachine == 2:
        print('EMPATOUUU!!! Também escolhi Papel')
    else:
        print('GANHEIII DE VOCÊ!!! Escolhi Tesoura')
else:
    if playmachine == 1:
        print('GANHEIII DE VOCÊ!!! Escolhi Pedra')
    elif playmachine == 2:
        print('DESSA VEZ EU PERDI!!! Escolhi Papel')
    else:
        print('EMPATOUUU!!! Também escolhi Tesoura')
