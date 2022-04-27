quant = 0
soma = 0

for num in range(1, 501):
    if num % 3 == 0 and num % 2 != 0:
        quant += 1
        soma += num

print('A soma de todos os {} valores solicitados é {}'.format(quant, soma))
