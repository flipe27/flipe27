def leia_int(frase):
    while True:
        num = input(frase).strip()
        while not num.isnumeric():
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            num = input(frase).strip()
        if num.isnumeric():
            break
    return int(num)


numero = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')
