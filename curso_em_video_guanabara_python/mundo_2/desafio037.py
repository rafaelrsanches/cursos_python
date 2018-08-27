# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('----------- CONVERSOR DE BASES -----------')
n = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
option = int(input('Você deseja converter para qual base? '))

if option == 1:
    print('{} convertido para BINÁRIO fica {}'.format(n, bin(n)[2:]))
elif option == 2:
    print('{} convertido para OCTAL fica {}'.format(n, oct(n)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL fica {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
