# Cadastro de Contato
contato = {}
contato["nome"] = input("Digite seu nome: ")
contato["numero"] = []

contato["numero"].append(input("Digite seu número: "))

respostaUsuario = input("Deseja adicionar mais um número? (sim/não): ").lower()
while respostaUsuario == "sim":
    contato["numero"].append(input("Digite seu número: "))
    respostaUsuario = input("Deseja adicionar mais um número? (sim/não)")
    
print(contato)