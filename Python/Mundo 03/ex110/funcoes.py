def formatar(num):
    valor = f'R${num:.2f}'.replace('.', ',')
    return valor


def aumento(num, taxa):
    num += (num * taxa / 100)
    return formatar(num)


def reducao(num, taxa):
    num -= (num * taxa / 100)
    return formatar(num)


def dobro(num):
    num *= 2
    return formatar(num)


def metade(num):
    num /= 2
    return formatar(num)


def resumo(num, aum, dim):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)

    print(f'{"Preço analisado:":<30}{formatar(num):>10}')
    print(f'{"Dobro do preço:":<30}{dobro(num):>10}')
    print(f'{"Metade do preço:":<30}{metade(num):>10}')
    print(f'{aum:02}{"% de aumento:":<28}{aumento(num, aum):>10}')
    print(f'{dim:02}{"% de redução:":<28}{reducao(num, dim):>10}')
    print('-' * 40)
