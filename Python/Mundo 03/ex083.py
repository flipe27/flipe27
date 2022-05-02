expressao = input('Digite a expressão: ')
quant_ida = quant_volta = 0
for cont in expressao:
    if cont == '(':
        quant_ida += 1
    if cont == ')':
        quant_volta += 1
if quant_ida == quant_volta:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
