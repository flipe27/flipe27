from funcoes import *

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.2f} é R${metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${dobro(preco):.2f}')
print(f'Aumentando 10%, temos {aumento(preco, 10):.2f}')
