# Soma de números pares
numeros = []
numeros.append(int(input("Digite o primeiro numero: ")))
numeros.append(int(input("Digite o segundo numero: ")))
numeros.append(int(input("Digite o terceiro numero: ")))
numeros.append(int(input("Digite o quarto numero: ")))
numeros.append(int(input("Digite o quinto numero: ")))

soma = 0
for i in numeros:
    if i % 2 == 0:
        soma += i  

print(soma)