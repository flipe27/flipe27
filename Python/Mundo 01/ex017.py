from math import sqrt

cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adj = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(cat_oposto, 2) + pow(cat_adj, 2))  # Pode usar diretamente também o "math.hypot()"

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
