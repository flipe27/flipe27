soma = 0
while True:  # O "Enquanto verdadeiro" vai rodar o programa infinitamente
    num = int(input('Digite um número: '))
    if num == 999:
        break  # Interrupção de um laço infinito
    else:
        soma += num
print(f'A soma vale {soma}')  # f-String
