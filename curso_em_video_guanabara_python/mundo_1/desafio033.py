# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Lê os números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Cria variáveis auxiliares
aux1 = n1
aux2 = n1

# Analisa o número maior
if n2 > n1 and n2 > n3:
    aux1 = n2
if n3 > n1 and n3 > n2:
    aux1 = n3

# Analisa o número menor
if n2 < n1 and n2 < n3:
    aux2 = n2
if n3 < n1 and n3 < n2:
    aux2 = n3

# Mostra o resultado
print('O maior número é {}'.format(aux1))
print('O menor número é {}'.format(aux2))
