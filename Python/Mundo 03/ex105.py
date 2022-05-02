def notas(*num, sit=False):
    """Função para analisar notas e situações de vários alunos.
    :param num: Uma ou várias notas dos alunos
    :param sit: Indicando se deve ou não adicionar a situação (opcional)
    :return: Dicionário com várias informações sobre a situação da turma"""
    aluno = dict()
    aluno['total'] = len(num)
    ordem = sorted(num)
    aluno['maior'] = ordem[-1]
    aluno['menor'] = ordem[0]

    soma = sum(num)
    aluno['media'] = soma / len(num)
    if sit:
        if aluno['media'] < 5:
            aluno['situacao'] = 'RUIM'
        elif aluno['media'] < 7:
            aluno['situacao'] = 'RAZOÁVEL'
        else:
            aluno['situacao'] = 'BOA'
    return aluno


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
