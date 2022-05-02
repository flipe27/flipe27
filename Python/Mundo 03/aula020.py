# Desempacotamento de parâmetro
def contador(*num):  # Dessa forma todos os parâmetros recebidos serão armazenados em "num"
    print(num)
    for cont in num:
        print(cont, end=' ')
    print('FIM!')


contador(5, 7, 2, 1)
contador(3, 9)
