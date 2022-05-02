def fatorial(num=1, show=False):
    """Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: Mostrar ou não a conta (opcional)
    :return: O valor do fatorial de um número 'num'"""

    print('-' * 30)
    if not show:
        resultado = 1
        for fat in range(num, 1, -1):
            resultado *= fat
    else:
        resultado = ''
        conta = 1
        for fat in range(num, 1, -1):
            resultado += f'{fat} x '
            conta *= fat
        resultado += f'1 = {conta}'
    return resultado


print(fatorial(5, True))
help(fatorial)
