soma = 0
quant = 0
for cont in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(cont)))
    if num % 2 == 0:
        soma += num
        quant += 1

print('Você informou {} números pares e a soma foi {}'.format(quant, soma))
