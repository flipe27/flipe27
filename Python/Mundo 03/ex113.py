def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        else:
            return num


def leia_real(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        else:
            return num


inteiro = leia_int('Digite um Inteiro: ')
real = leia_real('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
