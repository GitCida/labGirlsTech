# Contador Reverso
def contador_reverso(n):
    for i in range(n, -1, -1):
            print(i)

numero = int(input("Digite um número: "))
contador_reverso(numero)