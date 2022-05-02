jogador = dict()
gols = list()
jogador['nome'] = input('Nome do jogador: ').strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, partidas):
    gols.append(int(input(f'   Quantos gols na partida {cont}? ')))
jogador['gols'] = gols.copy()
soma = sum(gols)
jogador['total'] = soma

print('-' * 50)
print(jogador)
print('-' * 50)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')

print('-' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for pos, quant in enumerate(gols):
    print(f'  => Na partida {pos}, fez {quant} gols')
print(f'Foi um total de {jogador["total"]} gols.')
