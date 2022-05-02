from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram ', end='')
for cont in numeros:
    print(cont, end=' ')

ordem = sorted(numeros)
print(f'\nO maior valor sorteado foi {ordem[-1]}')  # Poderia também ter usado o "max()"
print(f'O menor valor sorteado foi {ordem[0]}')  # Poderia ter usado também o "min()"
