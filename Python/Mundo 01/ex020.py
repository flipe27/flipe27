import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)  # "shuffle()" vai embaralhar a lista de alunos

print('A ordem de apresentação será')
print(lista)
