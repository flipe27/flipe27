inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for cont in range(inicio, fim + 1, passo):
    print(cont)

print('Fim!')
