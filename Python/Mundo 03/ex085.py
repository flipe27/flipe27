pares = []
impares = []
for cont in range(0, 7):
    num = int(input(f'Digite o {cont + 1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('-' * 40)
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
