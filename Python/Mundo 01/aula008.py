n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro outro: '))

# "end" configura a quebra de linha e o "\n" cria uma quebra de linha
# ":.f" formata a quantidade de casas decimais
print('A soma é {}, \na multiplicação é {} e a divisão é {:.3f}'.format(n1 + n2, n1 * n2, n1 / n2), end=', ')
print('Divisão inteira {} e potência {}'.format(n1 // n2, n1 ** n2))
