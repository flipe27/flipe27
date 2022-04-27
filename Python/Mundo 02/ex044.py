print('{:-^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
pag = int(input('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if pag == 1:
    total = preco - (preco * 0.1)
elif pag == 2:
    total = preco - (preco * 0.05)
elif pag == 3:
    total = preco
    parcelas = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcelas))
elif pag == 4:
    total = preco + (preco * 0.2)
    quant_parcelas = int(input('Quantas parcelas? '))
    parcelas = total / quant_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(quant_parcelas, parcelas))
else:
    total = preco
    print('Opção inválida de pagamento, tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
