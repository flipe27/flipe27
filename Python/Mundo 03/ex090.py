aluno = dict()
aluno['nome'] = input('Nome: ').strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'

print('-' * 30)
for chave, valor in aluno.items():
    print(f' - {chave} é igual a {valor}')
    