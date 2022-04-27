from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for cont in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(cont)))
    if ano_atual - nasc < 18:
        menores += 1
    else:
        maiores += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))
