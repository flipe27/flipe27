print('Gerador de PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 0
mais = 10
mostrados = 10

while mais != 0:
    while cont < mais:
        print('{}'.format(a1), end=' → ')
        a1 += r
        cont += 1
    print('PAUSA')
    cont = 0
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    mostrados += mais
print('Progressão finalizada com {} termos mostrados.'.format(mostrados))
