filme = {'nome': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for chave, valor in filme.items():  # Para cada "chave" e "valor" dos "itens" do dicionário
    print(f'O {chave} é {valor}')
    