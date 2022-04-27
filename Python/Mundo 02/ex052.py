div = 0
num = int(input('Digite um número: '))

for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m{}\033[m'.format(cont), end=' ')
        div += 1
    else:
        print('\033[31m{}\033[m'.format(cont), end=' ')

print('\nO número {} foi divisível {} vezes'.format(num, div))
if div == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
