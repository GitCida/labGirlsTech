# Ler o Conteúdo de um Arquivo
with open("poema.txt", "w") as poema:
    poema.write("Quem me dera:\n")
    poema.write("Durmo inverno,\n")
    poema.write("Acordo primavera.\n")
    
with open("poema.txt", "r") as poema:
    conteudo = poema.read()
    print(conteudo)