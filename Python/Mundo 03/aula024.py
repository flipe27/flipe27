# Escopos
def local(b):
    b += 4  # A variável "b" por ser definida dentro de uma função tem escopo local
    global c  # "global" define que a variável usada não terá escopo local
    print(f'"a" existe em todo o programa e tem o valor {a}')
    print(f'"b" existe apenas localmente e vale {b}')
    print(f'"c" vale {c} globalmente')


# Programa principal
a = 5  # A variável "a" por ser definida no programa principal tem escopo global
c = 2  # "c" globalmente vale 2
local(5)
