salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    novo = salario + (salario * 0.1)
else:
    novo = salario + (salario * 0.15)

print('Quem ganhava R${:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))
