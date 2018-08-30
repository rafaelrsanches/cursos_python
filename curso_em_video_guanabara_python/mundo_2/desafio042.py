# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos lados diferentes.

print('Analisando a existência de um triângulo.')
l1 = float(input('Digite a medida da primeira reta: '))
l2 = float(input('Digite a medida da segunda reta: '))
l3 = float(input('Digite a medida da terceira reta: '))

if (abs(l2 - l3) < l1 < l2 + l3) or (abs(l1 - l3) < l2 < l1 + l3) or (abs(l1 - l2) < l3 < l1 + l2):
    print('Triângulo válido!')
    if l1 == l2 == l3:
        print('Triângulo EQUILÁTERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo ISÓSCELES!')
    else:
        print('Triângulo ESCALENO!')
else:
    print('Não foi possível formar um triângulo com essas medidas =(')
