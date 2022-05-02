def area(larg, comp):
    total = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {total:.1f} m².')


print(f'{" Controle de terrenos ":-^30}')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
