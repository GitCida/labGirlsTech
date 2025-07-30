# Copiar Conteúdo de um Arquivo para Outro
with open("original.txt", "w") as original:
    original.write("Conteúdo do arquivo original.\n")
    original.write("LabGirlsTech")

with open("original.txt", "r") as original:
    linhas = original.readlines()

with open("copia.txt", "w") as copia:
    for linha in linhas:
        copia.write(linha)