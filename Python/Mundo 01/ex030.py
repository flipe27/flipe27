num = int(input('Me diga um número qualquer: '))
print('O número {} é'.format(num), end=' ')
print('PAR' if num % 2 == 0 else 'ÍMPAR')
