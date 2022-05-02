from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

print('Sorteando valores:')
for chave, valor in jogadores.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)

# Ordenação inversa dos itens do dicionário "jogadores" a partir do item 1 (O item "0" é a chave e o "1" o valor)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{" RANKING DOS JOGADORES ":-^40}')
for cont in range(0, 4):
    print(f'{cont + 1}º lugar: {ranking[cont][0]} com {ranking[cont][1]}.')
