from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))

if idade < 18:
    anos = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(anos))
    print('Seu alistamento será em {}.'.format(ano_atual + anos))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    anos = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(anos))
    print('Seu alistamento foi em {}.'.format(ano_atual - anos))
