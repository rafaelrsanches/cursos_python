n = float(input('Digite uma distância em metros: '))

print('{:.1f}m corresponde a:\n{}km\n{}hm\n{:.0f}dam'.format(n, n/1000, n/100, n/10))
print('{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(n*10, n*100, n*1000))
