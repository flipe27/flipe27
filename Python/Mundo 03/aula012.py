pessoas = list()
dado = list()
for cont in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()  # "clear()" esvazia todos os itens da lista

for pessoa in pessoas:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
    else:
        print(f'{pessoa[0]} é menor de idade.')
