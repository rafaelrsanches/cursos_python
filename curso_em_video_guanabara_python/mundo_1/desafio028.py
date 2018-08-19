# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint # Importa o método randint
nu = int(input('Tente advinhar no número que estou pensando... Entre 0 e 5: ')) #Lê o palpite do usuário
na = randint(0, 5) #Sorteia um número aleatório entre 0 e 5
print('Você acertou!' if nu == na else 'Não foi dessa vez!') # Escreve na tela de acordo com a condição
