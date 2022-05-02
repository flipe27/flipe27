from funcoes import *

preco = float(input('Digite o preço: R$'))
print(f'A metade de {formatar(preco)} é {metade(preco)}')
print(f'O dobro de {formatar(preco)} é {dobro(preco)}')
print(f'Aumentando {10}%, temos {aumento(preco, 10)}')
