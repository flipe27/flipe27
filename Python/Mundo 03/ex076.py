print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Caneta', 22.3, 'Livro', 34.9)
for cont in range(0, len(produtos), 2):
    print(f'{produtos[cont]:.<30}R${produtos[cont + 1]:>8.2f}')
print('-' * 40)
