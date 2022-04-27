idades = 0
mulheres = 0
homem_velho = ''
idade_velho = 0

for pessoas in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoas))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    idades += idade

    if sexo in 'Mm' and idade > idade_velho:
        idade_velho = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

media = idades / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O home mais velho tem {} anos e se chama {}.'.format(idade_velho, homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
