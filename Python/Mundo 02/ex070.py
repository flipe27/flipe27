print('-' * 40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-' * 40)
soma = mais_mil = preco_barato = cont = 0
prod_barato = ''

while True:
    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$'))
    if cont == 0:
        preco_barato = preco
        prod_barato = produto
        cont += 1
    if preco < preco_barato:
        preco_barato = preco
        prod_barato = produto
    if preco > 1000:
        mais_mil += 1
    soma += preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_barato} que custa R${preco_barato:.2f}')
