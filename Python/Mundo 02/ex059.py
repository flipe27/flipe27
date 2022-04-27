from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
menu = 0

while menu != 5:
    print('''{:>9} somar
{:>9} multiplicar
{:>9} maior
{:>9} novos números
{:>9} sair do programa'''.format('[ 1 ]', '[ 2 ]', '[ 3 ]', '[ 4 ]', '[ 5 ]'))
    menu = int(input('>>>>> Qual é a sua opção? '))

    if menu == 5:
        print('Finalizando...')
    elif menu != 1 and menu != 2 and menu != 3 and menu != 4:
        print('Opção inválida. Tente novamente')
    else:
        if menu == 1:
            print('A soma entre {} + {} é {}'.format(num1, num2, num1 + num2))
        elif menu == 2:
            print('O resultado de {} x {} é {}'.format(num1, num2, num1 * num2))
        elif menu == 3:
            if num1 > num2:
                print('Entre {} e {} o maior valor é {}'.format(num1, num2, num1))
            elif num1 < num2:
                print('Entre {} e {} o maior valor é {}'.format(num1, num2, num2))
            else:
                print('Os dois números são iguais!')
        else:
            print('Informe os números novamente...')
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))

    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
