# Atualizar Arquivo (Sobrescrever)
with open("frases.txt", "w") as frases:
    frases.write("Conteúdo que vai ser sobrescrito.")
    
with open("frases.txt", "w") as frases:
    frases.write("Nova fase, novo código.")