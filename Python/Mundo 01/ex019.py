import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]  # Lista de elementos
sorteado = random.choice(lista)  # "choice()" sorteia um elemento de "lista"

print('O aluno escolhido foi {}'.format(sorteado))
