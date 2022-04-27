res = 'S'
while res == 'S':  # O laço vai ser até que o usuário insira um ponto de parada
    num = int(input('Digite um valor: '))
    res = input('Quer continuar? [S/N] ').upper()
print('Fim!')
