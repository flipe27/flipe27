numeros = list()
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
