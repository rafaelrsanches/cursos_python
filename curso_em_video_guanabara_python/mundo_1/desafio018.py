from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))
ânguloradi = radians(ângulo)

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ângulo, sin(ânguloradi)))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ângulo, cos(ânguloradi)))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(ângulo, tan(ânguloradi)))
