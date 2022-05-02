def formatar(num):
    moeda = f'R${num:.2f}'
    valor = moeda.replace('.', ',')
    return valor


def metade(num):
    num /= 2
    dividido = formatar(num)
    return dividido


def dobro(num):
    num *= 2
    dobrado = formatar(num)
    return dobrado


def aumento(num, taxa):
    num += (num * taxa / 100)
    aumentado = formatar(num)
    return aumentado
