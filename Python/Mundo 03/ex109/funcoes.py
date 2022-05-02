def formatar(num):
    moeda = f'R${num:.2f}'
    valor = moeda.replace('.', ',')
    return valor


def metade(num, formatado=False):
    num /= 2
    return num if not formatado else formatar(num)


def dobro(num, formatado=False):
    num *= 2
    return num if not formatado else formatar(num)


def aumento(num, taxa, formatado=False):
    num += (num * taxa / 100)
    return num if not formatado else formatar(num)
