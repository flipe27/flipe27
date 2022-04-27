from time import sleep
from random import randint

opcoes = ['Pedra', 'Papel', 'Tesoura']

jogador = int(input('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual é a sua jogada? '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

computador = randint(0, 2)
print('''-=-=-=-=-=-=-=-=-=-=-=-=
Computador jogou {}
Jogador jogou {}
-=-=-=-=-=-=-=-=-=-=-=-='''.format(opcoes[computador], opcoes[jogador]))

if (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('JOGADOR VENCE')
elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')
