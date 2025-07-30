# Escrever Lista de Compras
listaDeCompras = []
listaDeCompras.append("Papel higiênico")
listaDeCompras.append("Pasta de dente")
listaDeCompras.append("Farinha")
listaDeCompras.append("Chocolate")
listaDeCompras.append("Danone")

with open("compras.txt", "w") as compras:
    for item in listaDeCompras:
        compras.write(item + "\n")
