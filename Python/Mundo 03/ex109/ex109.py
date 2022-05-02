from funcoes import *

preco = float(input('Digite o preço: R$'))
print(f'A metade de {formatar(preco)} é {metade(preco, True)}')
print(f'O dobro de {formatar(preco)} é {dobro(preco, True)}')
print(f'Aumentando {10}%, temos {aumento(preco, 10)}')
