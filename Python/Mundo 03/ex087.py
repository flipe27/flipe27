matriz = [[], [], []]
pares = coluna3 = maior = 0
for cont in range(0, 3):
    coluna = 0
    while len(matriz[cont]) < 3:
        matriz[cont].append(int(input(f'Digite um valor para [{cont}, {coluna}]: ')))
        if matriz[cont][coluna] % 2 == 0:
            pares += matriz[cont][coluna]
        if coluna == 2:
            coluna3 += matriz[cont][coluna]
        if cont == 1:
            if matriz[cont][coluna] > maior:
                maior = matriz[cont][coluna]
        coluna += 1
print('-' * 30)

for mostrar in range(0, 3):
    for num in range(0, 3):
        print(f'[{matriz[mostrar][num]:^5}]', end=' ')
    print()

print('-' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior}')
