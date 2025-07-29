# Verificar Idade
def verificar_idade(idade):
    if idade < 18:
        return "Você é menor de idade."
    elif idade >=18 and idade < 60:
        return "Você é maior de idade."
    else:
        return "Você já é idoso(a)."

idade = int(input("Digite sua idade: "))
idadeVerificada = verificar_idade(idade)
print(idadeVerificada)