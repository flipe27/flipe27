estado = dict()
brasil = list()
for cont in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())  # "copy()" tem o mesmo papel do "[:]" para dicionários
    estado.clear()
print(brasil)
