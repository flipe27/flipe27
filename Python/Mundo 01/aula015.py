nome = input('Qual é o seu nome? ')

if nome == 'Paulo':  # Condição simples
    print('Que nome lindo você tem!')
else:  # "else" cria outro caminho possível, tornando a condição em composta
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(nome))
