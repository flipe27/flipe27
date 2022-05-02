a = [2, 3, 8, 1]
b = a
b[2] = 5  # Uma lista receber outra cria uma ligação entre elas
c = a[:]  # "c" recebe uma cópia dos valores de "a". Dessa forma não é criada a ligação entre as listas
c[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
