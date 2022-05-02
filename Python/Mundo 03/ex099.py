from time import sleep


def maior(*num):
    maior_num = 0
    print('-' * 40)
    print('Analisando os valores passados...')
    for cont in num:
        if cont > maior_num:
            maior_num = cont
        print(cont, end=' ')
        sleep(0.5)

    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {maior_num}.')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
