lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = lar*alt
tinta = area/2
print('Sua parede tem a dimensão {}m x {}m e sua área é de {}m².'.format(lar, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
