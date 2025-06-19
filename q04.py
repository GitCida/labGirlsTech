# Pode votar ou não?
idadeUsuario = int(input("Digite sua idade: "))

if idadeUsuario >= 16:
    print("Você pode votar!")
else:
    anosQueFaltam = 16 - idadeUsuario
    print(f'Você não pode votar ainda. Espere mais {anosQueFaltam} ano(s)')