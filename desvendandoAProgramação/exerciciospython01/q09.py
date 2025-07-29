# Soma de vários números (while com saída)
numero = float(input("Digite o primeiro número: "))
somaNumeros = 0

while numero != 0:
    somaNumeros += numero
    numero = float(input("Digite o próximo número: "))

print(f'A soma de todos esse números é: {somaNumeros}')