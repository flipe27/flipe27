import math  # Importação de todos os métodos do módulo "math"
from math import floor  # Importação apenas do método "floor" da biblioteca "math"

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrade de {} é igual a {}'.format(num, floor(raiz)))
