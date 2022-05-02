from random import randint
from time import sleep


def pares(lista):
    quant = 0
    for soma in lista:
        if soma % 2 == 0:
            quant += soma
    print(f'Somando os valores pares de {lista}, temos {quant}!')


def sortear():
    numeros = []
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        numeros.append(num)
        sleep(0.5)
    print('PRONTO!')
    pares(numeros)


sortear()
