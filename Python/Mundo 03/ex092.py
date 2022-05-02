from datetime import date
trabalhador = dict()
trabalhador['nome'] = input('Nome: ').strip()
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nasc

trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['contratacao'] + 35) - nasc

print('-' * 30)
for chave, valor in trabalhador.items():
    print(f' - {chave} tem o valor {valor}')
