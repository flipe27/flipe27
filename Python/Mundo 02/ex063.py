print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
num = int(input('Quantos termos você quer mostrar? '))
cont = num1 = 1
num2 = 0

print('~' * 30)
while cont <= num:
    if cont == 1:
        print('{}'.format(1), end=' → ')
    else:
        fib = num1 + num2
        num2 = num1
        num1 = fib
        print('{}'.format(fib), end=' → ')
    cont += 1
print('FIM')
print('~' * 30)
