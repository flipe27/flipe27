def jogador(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    jogador(gol=gols)
else:
    jogador(nome, gols)
