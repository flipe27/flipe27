print('=' * 30)
print(f'{"BANCO CEV":^30}')
print(f'=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
tot_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        tot_cedulas += 1
    else:
        if tot_cedulas > 0:
            print(f'Total de {tot_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            tot_cedulas = 0
            cedula = 20
        elif cedula == 20:
            tot_cedulas = 0
            cedula = 10
        elif cedula == 10:
            tot_cedulas = 0
            cedula = 1
        elif cedula == 1:
            tot_cedulas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
