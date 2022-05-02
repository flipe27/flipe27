# Tratamento de erros e exceções
try:  # Tente realizar esses comandos
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:  # Caso algum erro ocorra realize esses comandos
    print('Infelizmente tivemos um problema :(')
    print(f'Erro encontrado: {erro.__class__}')  # É possível definir outras configurações para o erro
else:  # Caso tudo tenha dado certo realize esses comandos
    print(f'O resultado é {r:.1f}')
finally:  # Independente se ocorreu ou não um erro realize esses comandos
    print('Volte sempre! Muito obrigado!')
