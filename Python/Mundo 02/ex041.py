from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('O atleta tem {} anos.'.format(idade))
print('Classificação: ', end='')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
