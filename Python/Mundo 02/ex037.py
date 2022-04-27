num = int(input('Digite um número inteiro: '))
base = int(input('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))

if base == 1:
    convertido = bin(num).replace('0b', '')
    print('{} convertido para BINÁRIO é igual a {}'.format(num, convertido))
elif base == 2:
    convertido = oct(num).replace('0o', '')
    print('{} convertido para OCTAL é igual a {}'.format(num, convertido))
elif base == 3:
    convertido = hex(num).replace('0x', '')
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, convertido))
else:
    print('Opção inválida! Tente novamente.')
