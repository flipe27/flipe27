# Docstrings
def contador(inicio, fim, passo):  # A função "contador()" passa a possuir uma pequena documentação
    """Faz uma contagem e mostra na tela.
    :param inicio: início da contagem
    :param fim: final da contagem
    :param passo: passo da contagem
    :return: sem retorno"""

    for cont in range(inicio, fim + 1, passo):
        print(cont, end=' ')
    print('FIM!')


contador(0, 10, 2)
help(contador)
