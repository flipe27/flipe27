times = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá', 'Internacional', 'Avaí', 'Bragantino',
         'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Fluminense', 'América-MG',
         'Ceará', 'Athletico-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')

print('-=' * 15)
print(f'Lista dos times do brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição')
