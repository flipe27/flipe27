pessoa = {}
grupo = []
idades = 0
while True:
    pessoa['nome'] = input('Nome: ').strip()
    pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo: [M/F] ')
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    grupo.append(pessoa.copy())

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 60)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = idades / len(grupo)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for cont in grupo:
    if cont['sexo'] == 'F':
        print(cont['nome'], end=' ')

print('\nD) Lista das pessoas que estão acima da média:')
for chec in grupo:
    if chec['idade'] > media:
        print(f'   nome = {chec["nome"]}; sexo = {chec["sexo"]}; idade = {chec["idade"]};')
print('<< ENCERRADO! >>')
