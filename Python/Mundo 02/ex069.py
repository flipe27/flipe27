mais18 = homens = mulheres20 = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)

    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-' * 30)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
