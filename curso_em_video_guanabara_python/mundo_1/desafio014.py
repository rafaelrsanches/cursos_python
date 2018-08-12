c = float(input('Digite a temperatura em ºC: '))

f = 1.8 * c + 32
k = c + 273

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(c, f))
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºK'.format(c, k))
