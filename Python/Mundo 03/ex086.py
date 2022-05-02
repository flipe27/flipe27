matriz = [[], [], []]
for cont in range(0, 3):
    row = 0
    while len(matriz[cont]) < 3:
        matriz[cont].append(int(input(f'Digite um valor para [{cont}, {row}]: ')))
        row += 1
print('-' * 30)
for mostrar in range(0, 3):
    for num in range(0, 3):
        print(f'[{matriz[mostrar][num]:^5}]', end=' ')
    print()
