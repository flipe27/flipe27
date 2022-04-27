frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
inverso = frase[::-1]  # Vai pegar a frase do início ao fim de trás pra frente
print('O inverso de {} é {}'.format(frase, inverso))

if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
