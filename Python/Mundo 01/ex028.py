import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

comp_num = random.randint(0, 5)
num = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if num == comp_num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp_num, num))
