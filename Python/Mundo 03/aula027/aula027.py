from modulos import fatorial, dobro, triplo  # Importação das funções de outro arquivo

numero = int(input('Digite um número: '))
fat = fatorial(numero)
print(f'O fatorial de {numero} é {fat}')
print(f'O dobro de {numero} é {dobro(numero)}')
print(f'O triplo de {numero} é {triplo(numero)}')
