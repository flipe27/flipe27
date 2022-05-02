valores = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-' * 30)
valores.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
