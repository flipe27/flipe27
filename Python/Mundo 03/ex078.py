numeros = list()
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('-' * 40)
print(f'Você digitou os valores {numeros}')
ordem = numeros[:]
ordem.sort()

print(f'O maior valor digitado foi {ordem[-1]} nas posições ', end='')
for pos, val in enumerate(numeros):
    if val == ordem[-1]:
        print(pos, end='... ')

print(f'\nO menor valor digitado foi {ordem[0]} nas posições ', end='')
for pos, val in enumerate(numeros):
    if val == ordem[0]:
        print(pos, end='... ')
