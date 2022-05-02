# Listas
numeros = [2, 5, 9, 1]
numeros[2] = 3  # Mudança do valor de um índice em uma lista
numeros.append(7)  # Adição do valor 7 como a última posição da lista
numeros.sort()  # Ordenação dos valores da lista. O parâmetro "reverse=True" ordenaria de forma decrescente
numeros.insert(2, 0)  # Adição do número 0 no índice 2
if 4 in numeros:
    numeros.remove(4)  # Remoção do valor 4 da lista
print(numeros)
print(f'Essa lista tem {len(numeros)} elementos')
