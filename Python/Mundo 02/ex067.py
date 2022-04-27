while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    else:
        print('-' * 30)
        for cont in range(1, 11):
            print(f'{num} x {cont:>2} = {num * cont}')
        print('-' * 30)
print('Programa TABUADA encerrado. Volte sempre!')
