# Outros tipos de transformações de strings
frase = '   Aprenda Python   '

print(frase)
print(frase.strip())  # Remove todos os espaços no início e no final da string
print(frase.rstrip())  # Remove apenas os espaços no final da string. Existe o "lstrip()" para remover os do início
print(frase.split())  # Divide a string, por padrão a partir dos espaços
print('-'.join(frase))  # Une todos os elementos da string ou da lista, nesse caso unindo com um "-"
