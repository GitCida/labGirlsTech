# Cadastro com Função
# Crie uma função cadastrar_usuario() que peça nome, idade e cidade ao usuário e
# retorne esses dados como um dicionário.
# Depois, imprima esse dicionário.
# Objetivo: Função que retorna um dicionário com dados do input.
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