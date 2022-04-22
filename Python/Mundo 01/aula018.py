# Algumas maneiras de trabalhar com as cores no terminal
nome = 'Paulo Fellipe'
game = '\033[33mChrono Trigger\033[m'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'violeta': '\033[35m'}

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(27, 12))
print('Olá muito prazer em te conhecer, {}{}{}!'.format('\033[34m', nome, '\033[m'))
print('Meu jogo favorito é {}!'.format(game))
print('Programar em {}Python{} é bom demais!'.format(cores['violeta'], cores['limpa']))
