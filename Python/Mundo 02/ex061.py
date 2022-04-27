print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 0

while cont < 10:
    print('{}'.format(a1), end=' → ')
    a1 += r
    cont += 1
print('FIM')
