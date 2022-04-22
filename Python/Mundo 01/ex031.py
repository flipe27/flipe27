km = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(km))
total = km * 0.45 if km > 200 else km * 0.5
print('E o preço da sua passagem será de R${:.2f}'.format(total))
