from time import sleep


def pyhelp(ajuda):
    titulo(f'Acessando o manual do comando "{ajuda}"', 4)
    print(cores[6], end='')
    help(ajuda)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


cores = ('\033[m',    # Sem cor
         '\033[41m',  # Vermelho
         '\033[42m',  # Verde
         '\033[43m',  # Amarelo
         '\033[44m',  # Azul
         '\033[45m',  # Roxo
         '\033[7m')   # Branco

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    opcao = input('Função ou biblioteca > ').strip()
    if opcao.upper() == 'FIM':
        break
    else:
        pyhelp(opcao)
titulo('ATÉ LOGO!', 1)
