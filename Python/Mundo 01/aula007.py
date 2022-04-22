nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:^20}!'.format(nome))  # É possível formatar quantos espaços o parâmetro vai ocupar
print('{:-^20}'.format(nome))  # É possível também preencher os espaços vazios
