# Cadastro com Função
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digita sua cidade: ")
    dados = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    return dados

print(cadastrar_usuario())