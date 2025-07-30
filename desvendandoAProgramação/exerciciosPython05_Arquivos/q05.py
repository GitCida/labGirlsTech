# Contar Linhas de um Arquivo
with open("dados.txt", "w") as dados:
    dados.write("dados 1\n")
    dados.write("dados 2\n")
    dados.write("dados 3\n")
    dados.write("dados 4")

with open("dados.txt", "r") as dados:
    linhas = dados.readlines()
    x = len(linhas)
    print(x)