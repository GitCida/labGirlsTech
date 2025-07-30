# Exibir Somente as Linhas Pares
with open("texto.txt", "w") as texto:
    texto.write("Linha 1\n")
    texto.write("Linha 2\n")
    texto.write("Linha 3\n")
    texto.write("Linha 4\n")
    texto.write("Linha 5\n")
    texto.write("Linha 6")

with open("texto.txt", "r") as texto:
    linhas = texto.readlines()
    for i, item in enumerate(linhas):
        if i % 2 != 0:
            print(f'{i+1}. {item.strip()}')