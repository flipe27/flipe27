num = int(input('Informe um número: '))

print('Analisando o número', num)

milhar = num // 1000
centena = (num % 1000) // 100
dezena = ((num % 1000) % 100) // 10
unidade = ((num % 1000) % 100) % 10

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
