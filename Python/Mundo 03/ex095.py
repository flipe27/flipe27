jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = input('Nome do jogador: ').strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(0, jogador['partidas']):
        gols.append(int(input(f'   Quantos gols na partida {cont + 1}? ')))
    jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    gols.clear()

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 45)
print(f'{"cod":3} {"nome":16} {"gols":18} {"total":5}')
print('-' * 45)
cod = 0
for mostrar in jogadores:
    print(f'{cod:<3} {mostrar["nome"]:16} {str(mostrar["gols"]):18} {sum(mostrar["gols"]):>5}')
    cod += 1

while True:
    num = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    while num > len(jogadores) - 1 or num < 0:
        print(f'ERRO! Não existe jogador com o código {num}!')
        num = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    if num == 999:
        break
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {jogadores[num]["nome"]}:')
        for pos, valor in enumerate(jogadores[num]['gols']):
            print(f'     No jogo {pos + 1} fez {valor} gols.')
print('<< VOLTE SEMPRE! >>')
