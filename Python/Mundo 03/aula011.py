pessoas = [['Pedro', 25], ['Maria', 19], ['João, 32']]  # É possível organizar listas dentro de outras listas
dev = ['Paulo', 19]
pessoas.append(dev[:])
print(pessoas[3][0])
