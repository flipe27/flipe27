num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
print('Calculando {0}! = {0}'.format(num), end='')

while num > 1:
    fatorial *= num
    num -= 1
    print(' x {}'.format(num), end='')
print(' = {}'.format(fatorial))
