try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):  # É possível definir os erros esperados
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:  # Um "try" pode ter vários "except"
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
