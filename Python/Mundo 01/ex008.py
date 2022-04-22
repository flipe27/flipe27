metros = float(input('Uma distância em metros: '))

print('A medida de {}m corresponde a'.format(metros))
print('{}km\n{}hm\n{}dam'.format(metros / 1000, metros / 100, metros / 10))
print('{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(metros * 10, metros * 100, metros * 1000))
