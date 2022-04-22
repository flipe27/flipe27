# Análise de strings
frase = 'Curso em Video Python'

print(len(frase))  # Mostra a quantidade de caracteres da string
print(frase.count('o'))  # Conta quantas vezes o parâmetro aparece na string
print(frase.count('o', 0, 14))  # É possível também definnir um intervalo para a contagem
print(frase.find('deo'))  # Indica o indíce da primeira aparição do parâmetro informado
print(frase.find('Android'))  # Caso o parâmetro não exista na string a função retorna o valor "-1"
print('Curso' in frase)  # Verifica se "Curso" existe na string e retorna True ou False
