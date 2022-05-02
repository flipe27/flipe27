from time import sleep


def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim > inicio:
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=' ')
            sleep(0.5)
    elif inicio > fim:
        for cont in range(inicio, fim - 1, passo * -1):
            print(cont, end=' ')
            sleep(0.5)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
comeco = int(input(f'{"Início:":<8}'))
final = int(input(f'{"Fim:":<8}'))
pulo = int(input(f'{"Passo:":<8}'))
contagem(comeco, final, pulo)
