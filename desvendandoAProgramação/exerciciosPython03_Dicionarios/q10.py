# Frequência de Letras
# Peça ao usuário uma palavra. Crie um dicionário que mostre quantas vezes cada letra
# aparece.
# Objetivo: Lógica com dicionário, contagem e laço for.
palavra = input("Digite uma palavra: ")
letras = {}

for letra in palavra:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

print(letras)