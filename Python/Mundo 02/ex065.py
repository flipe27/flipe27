continuar = 'S'
quant = soma = maior = menor = 0

while continuar != 'N':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input('Quer continuar? [S/N] ').strip().upper()

print('Você digitou {} números e a média foi {:.2f}'.format(quant, (soma / quant)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
