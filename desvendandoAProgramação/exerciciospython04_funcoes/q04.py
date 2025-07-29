# Calculadora Simples
def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação(+, -, *, /): ")
resultado = calculadora(n1, n2, operacao)

if operacao != "+" or operacao != "-" or operacao != "*" or operacao != "/":
    print("Digite uma operação válida.")
else:
    print(f'O resultado de {n1} {operacao} {n2} é {resultado}')