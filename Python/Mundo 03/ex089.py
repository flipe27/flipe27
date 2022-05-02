alunos = []
dados = []
notas = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-' * 30)
print(f'{"No.":4}{"NOME":18}{"MÉDIA":>8}')
for cont in range(0, len(alunos)):
    media = (alunos[cont][1] + alunos[cont][2]) / 2
    print(f'{cont:<4}{alunos[cont][0]:18}{media:>8.1f}')
print('-' * 30)

while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    else:
        notas.append(alunos[num][1])
        notas.append(alunos[num][2])
        print(f'Notas de {alunos[num][0]} são {notas}')
        notas.clear()
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
