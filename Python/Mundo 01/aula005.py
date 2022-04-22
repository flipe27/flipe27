n1 = int(input('Digite um valor: '))  # "int()" vai transformar seu parâmetro em um número inteiro
print(type(n1))  # "type()" mostra o tipo primitivo do seu parâmetro

n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))  # É possível também definir a ordem de aparição
