numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
