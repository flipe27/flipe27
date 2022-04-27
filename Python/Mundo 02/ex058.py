from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

comp = randint(0, 10)
num = int(input('Qual é o seu palpite? '))
tentativas = 1

while num != comp:
    if num < comp:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    num = int(input('Qual é o seu palpite? '))
    tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
