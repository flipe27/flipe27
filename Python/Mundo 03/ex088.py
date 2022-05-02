from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {jogos} JOGOS  -=-=-=')

sorteados = []
for cont in range(0, jogos):
    for num in range(0, 6):
        escolhido = randint(1, 60)
        while escolhido not in sorteados:
            sorteados.append(escolhido)
    sorteados.sort()

    print(f'Jogo {cont + 1}: {sorteados}')
    sorteados.clear()
    sleep(1)
print(f'{" < BOA SORTE! > ":-^33}')
