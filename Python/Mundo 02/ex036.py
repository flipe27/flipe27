valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacoes = valor / (anos * 12)
porcent = salario * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacoes))

if prestacoes >= porcent:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
