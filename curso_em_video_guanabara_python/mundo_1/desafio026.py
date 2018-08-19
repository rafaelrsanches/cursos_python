# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra 'A'.
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase: ')).upper().strip() # Lê a frase, coloca em maiúsculo e tira os espaços excedentes
print('A letra A aparece {} vezes na frase'.format(phrase.count('A'))) # Conta o número de letras A
print('A letra A aparece a primeira vez na posição {}'.format(phrase.find('A') + 1)) # Encontra a posição da 1ª letra A
print('A letra A aparece a última vez na posição {}'.format(phrase.rfind('A') + 1)) # Encontra a posição da última letra A
