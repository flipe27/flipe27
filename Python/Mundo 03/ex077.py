palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso',
            'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',
            'Programador', 'Futuro')
for cont in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[cont].upper()} temos ', end='')
    for vogais in range(0, len(palavras[cont])):
        if palavras[cont][vogais].lower() in 'aeiou':
            print(palavras[cont][vogais].lower(), end=' ')
