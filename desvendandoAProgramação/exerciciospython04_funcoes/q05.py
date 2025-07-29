# Maior Número
def maior_valor(x, y):
    if x > y:
        return x
    elif x < y:
        return y
            
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))

maiorNumero = maior_valor(n1, n2)
print(f'{maiorNumero} tem o maior valor.')
