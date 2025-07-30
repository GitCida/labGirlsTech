# Salvar Notas em Arquivo
nome = input("Digite seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3)/3
with open("notas.txt", "w") as notas:
    notas.write(f'{nome} - Média: {media:.2F}')