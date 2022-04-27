from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    opcao = ' '
    while opcao not in 'PI':
        opcao = input('Par ou ímpar? [P/I] ').strip().upper()
    print('-' * 30)

    print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} ', end='')
    if opcao == 'P':
        if (jogador + computador) % 2 == 0:
            print('DEU PAR!\nVOCÊ VENCEU!')
            vitorias += 1
        else:
            print('DEU ÍMPAR!\nVOCÊ PERDEU!')
            break
    else:
        if (jogador + computador) % 2 != 0:
            print('DEU ÍMPAR!\nVOCÊ VENCEU!')
            vitorias += 1
        else:
            print('DEU PAR!\nVOCÊ PERDEU!')
            break
    print('=-' * 15)
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes.')
