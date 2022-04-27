nome = input('Qual é o seu nome? ')

if nome == 'Paulo':
    print('Que nome bonito.')
elif nome == 'Ana':  # Condicional aninhada utilizando o "elif"
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))
