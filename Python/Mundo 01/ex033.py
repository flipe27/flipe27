num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

lista = [num1, num2, num3]
ordem = sorted(lista)  # "sorted()" vai ordenar os valores de "lista"

print('O menor valor digitado foi {}'.format(ordem[0]))
print('O maior valor digitado foi {}'.format(ordem[2]))
