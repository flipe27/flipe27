pessoas = []
dado = []
quant = maior = menor = 0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    quant += 1

    if quant == 1:
        maior = menor = dado[1]
    if dado[1] > maior:
        maior = dado[1]
    if dado[1] < menor:
        menor = dado[1]
    dado.clear()

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-' * 30)
print(f'Ao todo, você cadastrou {quant} pessoas.')

print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for cont in pessoas:
    if cont[1] == maior:
        print(f'[{cont[0]}]', end=' ')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for cont in pessoas:
    if cont[1] == menor:
        print(f'[{cont[0]}]', end=' ')
